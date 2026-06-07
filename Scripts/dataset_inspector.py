import json
import numpy as np
import pandas as pd


class NpEncoder(json.JSONEncoder):
    """Энкодер для безопасной конвертации типов NumPy в нативный JSON."""

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (np.bool_, bool)):
            return bool(obj)
        return super(NpEncoder, self).default(obj)


def analyze_dataset(df_or_path, target_column=None, max_categories_sample=5):
    """Выполняет глубокий базовый анализ датасета.

    Исправлен варнинг select_dtypes() для совместимости с Pandas 3.x/4.x.
    """
    # 1. Загрузка данных
    if isinstance(df_or_path, str):
        if df_or_path.endswith(".csv"):
            df = pd.read_csv(df_or_path)
        elif df_or_path.endswith(".parquet"):
            df = pd.read_parquet(df_or_path)
        else:
            raise ValueError(
                "Неподдерживаемый формат файла. Передайте DataFrame, CSV или Parquet."
            )
    elif isinstance(df_or_path, pd.DataFrame):
        df = df_or_path.copy()
    else:
        raise TypeError("Ожидался путь к файлу или pd.DataFrame.")

    # 2. Сбор общих метрик
    total_rows, total_cols = df.shape
    duplicate_rows = int(df.duplicated().sum())
    memory_usage = float(df.memory_usage(deep=True).sum() / (1024**2))

    # БЕЗОПАСНОЕ РАЗДЕЛЕНИЕ ТИПОВ (Решает проблему с Pandas4Warning)
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    dt_cols = df.select_dtypes(
        include=["datetime", "datetimetz"]
    ).columns.tolist()

    # Все, что не число и не дата — относится к категориальным/текстовым признакам
    cat_cols = [c for c in df.columns if c not in num_cols and c not in dt_cols]

    # 3. Анализ колонок
    columns_summary = {}
    constant_columns = []
    high_cardinality_cats = []

    for col in df.columns:
        col_data = df[col]
        dtype = str(col_data.dtype)
        missing_count = int(col_data.isna().sum())
        missing_pct = round((missing_count / total_rows) * 100, 2)
        unique_count = int(col_data.nunique())

        if unique_count <= 1:
            constant_columns.append(col)

        stats = {"dtype": dtype, "missing_pct": missing_pct, "nunique": unique_count}

        # Статистика для численных данных
        if col in num_cols:
            stats["type"] = "numerical"
            stats["min"] = (
                float(col_data.min()) if not pd.isna(col_data.min()) else None
            )
            stats["max"] = (
                float(col_data.max()) if not pd.isna(col_data.max()) else None
            )
            stats["mean"] = (
                float(col_data.mean()) if not pd.isna(col_data.mean()) else None
            )
            stats["zeros_pct"] = round(
                (int((col_data == 0).sum()) / total_rows) * 100, 2
            )

        # Статистика для категориальных/текстовых данных
        elif col in cat_cols:
            stats["type"] = "categorical"

            # Если уникальных значений много и это не булев тип — это потенциальный ID/Хеш
            if (
                unique_count > 100
                and "bool" not in dtype
                and "boolean" not in dtype
            ):
                high_cardinality_cats.append(col)

            top_vals = col_data.value_counts().head(max_categories_sample)
            stats["sample_values"] = {
                str(k): int(v) for k, v in top_vals.to_dict().items()
            }

        # Статистика для дат
        elif col in dt_cols:
            stats["type"] = "datetime"
            stats["min"] = str(col_data.min())
            stats["max"] = str(col_data.max())

        columns_summary[col] = stats

    # Анализ целевой переменной
    target_info = None
    if target_column and target_column in df.columns:
        raw_dist = df[target_column].value_counts(normalize=True).head(5)
        clean_dist = {str(k): float(v) for k, v in raw_dist.items()}
        target_info = {
            "name": target_column,
            "type": columns_summary[target_column]["type"],
            "distribution": clean_dist,
        }

    # =========================================================================
    # ВЫВОД ДЛЯ ЧЕЛОВЕКА
    # =========================================================================
    print("=" * 80)
    print(f" СВОДНЫЙ ОТЧЕТ ПО ДАТАСЕТУ ".center(80, "#"))
    print("=" * 80)
    print(f"Размерность: {total_rows} строк | {total_cols} колонок")
    print(
        f"Типы признаков: Численных: {len(num_cols)} | Категориальных: {len(cat_cols)} | Временных: {len(dt_cols)}"
    )
    print(
        f"Дубликаты строк: {duplicate_rows} ({round((duplicate_rows/total_rows)*100, 2)}%)"
    )
    print(f"Объем в памяти: {round(memory_usage, 2)} MB")
    print("-" * 80)

    print(" ОБНАРУЖЕННЫЕ АНОМАЛИИ И ПРОБЛЕМЫ: ")
    has_issues = False
    if constant_columns:
        print(f" ->  Константные колонки (бесполезные): {constant_columns}")
        has_issues = True
    if high_cardinality_cats:
        print(
            f" ->  Высокая кардинальность текста (возможен ID/Хеш): {high_cardinality_cats}"
        )
        has_issues = True

    cols_with_missing = [
        c for c, v in columns_summary.items() if v["missing_pct"] > 0
    ]
    if cols_with_missing:
        print(" ->  Колонки с пропусками данных:")
        for c in cols_with_missing:
            print(f"    * {c}: {columns_summary[c]['missing_pct']}% пропусков")
        has_issues = True

    if not has_issues:
        print(" -> Критических базовых аномалий не обнаружено.")
    print("-" * 80)

    print(" ДЕТАЛЬНЫЙ АНАЛИЗ КОЛОНОК: ")
    human_table = []
    for col, info in columns_summary.items():
        missing = f"{info['missing_pct']}%"
        uniq = info["nunique"]
        if info["type"] == "numerical":
            details = f"Min: {info['min']} | Max: {info['max']} | Mean: {round(info['mean'], 2) if info['mean'] else 'N/A'}"
        elif info["type"] == "categorical":
            details = f"Cats: {list(info['sample_values'].keys())[:3]}..."
        else:
            details = f"Range: {info['min']} -> {info['max']}"

        human_table.append(
            {
                "Колонка": col,
                "Тип": info["dtype"],
                "Пропуски": missing,
                "Уникальных": uniq,
                "Детали / Границы": details,
            }
        )

    print(pd.DataFrame(human_table).to_string(index=False))
    print("=" * 80)

    # =========================================================================
    # ВЫВОД ДЛЯ ИИ
    # =========================================================================
    ai_context = {
        "dataset_metadata": {
            "shape": {"rows": total_rows, "columns": total_cols},
            "duplicates_count": duplicate_rows,
            "feature_types_count": {
                "numerical": len(num_cols),
                "categorical": len(cat_cols),
                "datetime": len(dt_cols),
            },
            "anomalies": {
                "constant_columns": constant_columns,
                "high_cardinality_categorical": high_cardinality_cats,
            },
        },
        "target_variable": target_info,
        "columns_detailed_schema": columns_summary,
    }

    ai_json_output = json.dumps(
        ai_context, indent=2, ensure_ascii=False, cls=NpEncoder
    )

    return ai_json_output


data = pd.read_csv("../data/raw/lora_request_trace.csv")
# Запуск анализа
ai_prompt_context = analyze_dataset(data, target_column="prompt_length")

print(ai_prompt_context)