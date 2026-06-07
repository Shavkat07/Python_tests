# 🎬 Инструменты для подготовки датасета из видео

Набор скриптов для извлечения кадров из видео и их лейблинга для обучения CNN моделей.

## 📋 Требования

```bash
pip install opencv-python
```

## 🚀 Быстрый старт

### 1️⃣ Извлечение кадров

**Базовое использование (каждую секунду):**
```bash
python video_frame_extractor.py video.mp4
```

Для вашего видео (3 мин 53 сек = 233 секунды):
- Интервал 1 сек → ~233 кадра
- Интервал 2 сек → ~116 кадров
- Интервал 0.5 сек → ~466 кадров

### 2️⃣ Лейблинг кадров

```bash
python frame_labeler.py frames -l "defect" "ok"
```

---

## 📖 Подробные примеры

### Извлечение кадров

#### Пример 1: Умеренное количество (каждые 2 секунды)
```bash
python video_frame_extractor.py video.mp4 -i 2.0 -o frames_2sec
```
**Результат:** ~116 кадров

#### Пример 2: С пропуском начала/конца
```bash
python video_frame_extractor.py video.mp4 -i 1.0 --skip-start 10 --skip-end 10 -o frames_clean
```
**Результат:** Пропустит первые и последние 10 секунд

#### Пример 3: Ограничить количество + ресайз
```bash
python video_frame_extractor.py video.mp4 -i 0.5 --max 200 --width 640 -o frames_resized
```
**Результат:** Максимум 200 кадров, ширина 640px

#### Пример 4: Высокое качество, большой интервал
```bash
python video_frame_extractor.py video.mp4 -i 3.0 -q 100 --width 1280 -o frames_hq
```
**Результат:** ~77 кадров в высоком качестве

#### Пример 5: С превью (чтобы посмотреть что извлекается)
```bash
python video_frame_extractor.py video.mp4 -i 1.0 --preview
```

### Лейблинг

#### Пример 1: Бинарная классификация
```bash
python frame_labeler.py frames_2sec -l "defect" "normal"
```
Управление:
- `1` - defect
- `2` - normal
- `s` - пропустить
- `q` - сохранить и выйти

#### Пример 2: Многоклассовая задача
```bash
python frame_labeler.py frames_2sec -l "scratch" "dent" "crack" "ok" "unsure"
```

#### Пример 3: Продолжить работу
```bash
python frame_labeler.py frames_2sec -l "defect" "ok" --start 50
```
Начнет с 51-го кадра

#### Пример 4: Свой файл меток
```bash
python frame_labeler.py frames_2sec -l "good" "bad" -o my_dataset_labels.json
```

---

## 🎯 Рекомендуемые стратегии

### Для вашего видео (3:53, >500 МБ):

#### Стратегия 1: Быстрая разметка (150-200 кадров)
```bash
# Извлечь
python video_frame_extractor.py video.mp4 -i 1.5 -o frames_medium

# Разметить
python frame_labeler.py frames_medium -l "defect" "ok"
```

#### Стратегия 2: Детальная разметка (300-400 кадров)
```bash
# Извлечь
python video_frame_extractor.py video.mp4 -i 0.75 -o frames_detailed

# Разметить
python frame_labeler.py frames_detailed -l "type1" "type2" "type3"
```

#### Стратегия 3: Сбалансированная (200 кадров + ресайз)
```bash
# Извлечь с ресайзом для экономии места
python video_frame_extractor.py video.mp4 -i 1.2 --width 800 -o frames_balanced

# Разметить
python frame_labeler.py frames_balanced -l "defect" "ok"
```

#### Стратегия 4: Эксперимент (начните с малого)
```bash
# Сначала извлеките мало
python video_frame_extractor.py video.mp4 -i 5.0 -o frames_test

# Разметьте быстро
python frame_labeler.py frames_test -l "class1" "class2"

# Если интервал хороший - увеличьте датасет
python video_frame_extractor.py video.mp4 -i 2.0 -o frames_full
```

---

## 📊 Формат выходных данных

### Структура директорий
```
frames/
  ├── frame_00000_t0.00s.jpg
  ├── frame_00001_t1.00s.jpg
  ├── frame_00002_t2.00s.jpg
  └── ...

labels.json
```

### Формат labels.json
```json
{
  "metadata": {
    "created": "2024-01-15T10:30:00",
    "last_updated": "2024-01-15T11:45:00",
    "labels": ["defect", "ok"],
    "total_labeled": 150
  },
  "annotations": {
    "frame_00000_t0.00s.jpg": {
      "label": "ok",
      "frame_path": "frames/frame_00000_t0.00s.jpg",
      "labeled_at": "2024-01-15T10:35:00"
    },
    "frame_00001_t1.00s.jpg": {
      "label": "defect",
      "frame_path": "frames/frame_00001_t1.00s.jpg",
      "labeled_at": "2024-01-15T10:36:00"
    }
  }
}
```

---

## ⌨️ Управление в лейблере

| Клавиша | Действие |
|---------|----------|
| `1-9` | Присвоить метку (номер в списке) |
| `s` | Пропустить кадр |
| `b` | Вернуться назад |
| `d` | Удалить метку текущего кадра |
| `h` | Показать справку |
| `q` | Сохранить и выйти |

---

## 🔧 Дополнительные опции

### video_frame_extractor.py

```bash
python video_frame_extractor.py --help
```

| Параметр | Описание | Пример |
|----------|----------|--------|
| `video` | Путь к видео | `video.mp4` |
| `-o` | Выходная папка | `-o frames` |
| `-i` | Интервал в секундах | `-i 1.5` |
| `--skip-start` | Пропустить начало (сек) | `--skip-start 10` |
| `--skip-end` | Пропустить конец (сек) | `--skip-end 5` |
| `--max` | Макс. количество кадров | `--max 200` |
| `-q` | Качество JPEG (0-100) | `-q 95` |
| `--width` | Ширина ресайза | `--width 640` |
| `--height` | Высота ресайза | `--height 480` |
| `--preview` | Показывать превью | `--preview` |

### frame_labeler.py

```bash
python frame_labeler.py --help
```

| Параметр | Описание | Пример |
|----------|----------|--------|
| `frames_dir` | Папка с кадрами | `frames` |
| `-l` | Список меток | `-l "ok" "bad"` |
| `-o` | Файл меток | `-o labels.json` |
| `--start` | Начать с кадра N | `--start 50` |

---

## 💡 Советы

1. **Начните с большого интервала** (3-5 сек), оцените качество датасета
2. **Используйте ресайз** если исходное разрешение очень большое
3. **Пропускайте начало/конец** если там нет полезной информации
4. **Сохраняйте промежуточно** - лейблер сохраняет после каждого выхода
5. **Используйте превью** при первом извлечении чтобы подобрать интервал

## 🎓 Использование в обучении CNN

После разметки можете использовать данные так:

```python
import json
from pathlib import Path

# Загрузить метки
with open('labels.json') as f:
    data = json.load(f)

# Создать датасет
images = []
labels = []

for filename, info in data['annotations'].items():
    images.append(info['frame_path'])
    labels.append(info['label'])

# Далее используйте с PyTorch/TensorFlow/Keras
```

---

## 📈 Оценка размера датасета

Для видео 3:53 (233 секунды):

| Интервал | Кадров | Примерный размер* |
|----------|--------|-------------------|
| 0.5 сек | ~466 | ~70-140 МБ |
| 1.0 сек | ~233 | ~35-70 МБ |
| 1.5 сек | ~155 | ~23-46 МБ |
| 2.0 сек | ~116 | ~17-35 МБ |
| 3.0 сек | ~77 | ~12-23 МБ |
| 5.0 сек | ~46 | ~7-14 МБ |

*Зависит от содержимого и качества сжатия

---

## ❓ FAQ

**Q: Сколько кадров нужно для обучения CNN?**  
A: Зависит от задачи. Начните с 200-300 для простых задач.

**Q: Какой интервал выбрать?**  
A: Зависит от скорости изменения сцены. Если объекты меняются быстро - меньше интервал.

**Q: Можно ли продолжить разметку позже?**  
A: Да, используйте `--start N` для продолжения с нужного кадра.

**Q: Как изменить разрешение кадров?**  
A: Используйте `--width` или `--height` при извлечении.

---

Удачи в подготовке датасета! 🚀
