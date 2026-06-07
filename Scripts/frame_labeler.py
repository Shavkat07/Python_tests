#!/usr/bin/env python3
"""
Интерактивный инструмент для лейблинга кадров
Позволяет быстро размечать извлеченные кадры для обучения CNN
"""

import cv2
import os
import json
from pathlib import Path
import argparse
from datetime import datetime


class FrameLabeler:
    def __init__(self, frames_dir, labels, output_json="labels.json", start_from=0):
        """
        Инициализация лейблера
        
        Параметры:
        -----------
        frames_dir : str
            Директория с кадрами
        labels : list
            Список возможных меток (например: ['cat', 'dog', 'bird'])
        output_json : str
            Файл для сохранения меток
        start_from : int
            С какого кадра начать (для продолжения работы)
        """
        self.frames_dir = Path(frames_dir)
        self.labels = labels
        self.output_json = output_json
        self.start_from = start_from
        
        # Загружаем существующие метки если есть
        self.labeled_data = self.load_labels()
        
        # Получаем список кадров
        self.frames = sorted([
            f for f in self.frames_dir.glob("*.jpg")
        ] + [
            f for f in self.frames_dir.glob("*.png")
        ])
        
        if not self.frames:
            raise ValueError(f"Не найдено кадров в {frames_dir}")
        
        self.current_idx = start_from
        self.total_frames = len(self.frames)
        
    def load_labels(self):
        """Загружает существующие метки из JSON"""
        if os.path.exists(self.output_json):
            with open(self.output_json, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "metadata": {
                "created": datetime.now().isoformat(),
                "labels": self.labels
            },
            "annotations": {}
        }
    
    def save_labels(self):
        """Сохраняет метки в JSON"""
        self.labeled_data["metadata"]["last_updated"] = datetime.now().isoformat()
        self.labeled_data["metadata"]["total_labeled"] = len(self.labeled_data["annotations"])
        
        with open(self.output_json, 'w', encoding='utf-8') as f:
            json.dump(self.labeled_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 Сохранено в {self.output_json}")
    
    def get_stats(self):
        """Статистика по меткам"""
        stats = {}
        for data in self.labeled_data["annotations"].values():
            label = data["label"]
            stats[label] = stats.get(label, 0) + 1
        return stats
    
    def print_help(self):
        """Выводит справку по управлению"""
        print("\n" + "="*60)
        print("УПРАВЛЕНИЕ:")
        print("="*60)
        for i, label in enumerate(self.labels, 1):
            print(f"  {i} - {label}")
        print(f"  s - пропустить кадр (skip)")
        print(f"  b - вернуться назад (back)")
        print(f"  d - удалить метку текущего кадра (delete)")
        print(f"  h - показать эту справку (help)")
        print(f"  q - сохранить и выйти (quit)")
        print("="*60)
    
    def draw_info(self, frame, filename):
        """Рисует информацию на кадре"""
        frame = frame.copy()
        h, w = frame.shape[:2]
        
        # Фон для текста
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (w, 100), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
        
        # Информация
        info_text = f"Кадр {self.current_idx + 1}/{self.total_frames}: {filename}"
        cv2.putText(frame, info_text, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Текущая метка если есть
        if filename in self.labeled_data["annotations"]:
            current_label = self.labeled_data["annotations"][filename]["label"]
            label_text = f"Текущая метка: {current_label}"
            cv2.putText(frame, label_text, (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            label_text = "Не размечен"
            cv2.putText(frame, label_text, (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Прогресс
        stats = self.get_stats()
        stats_text = " | ".join([f"{label}: {count}" for label, count in stats.items()])
        cv2.putText(frame, stats_text, (10, 90), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
        
        return frame
    
    def run(self):
        """Запускает интерактивный процесс лейблинга"""
        self.print_help()
        
        print(f"\nНайдено {self.total_frames} кадров")
        print(f"Уже размечено: {len(self.labeled_data['annotations'])}")
        print(f"Начинаем с кадра {self.current_idx + 1}\n")
        print("Нажмите 'h' для справки\n")
        
        window_name = "Frame Labeler"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        
        while self.current_idx < self.total_frames:
            frame_path = self.frames[self.current_idx]
            filename = frame_path.name
            
            # Загружаем кадр
            frame = cv2.imread(str(frame_path))
            if frame is None:
                print(f"⚠️  Не удалось загрузить {filename}")
                self.current_idx += 1
                continue
            
            # Добавляем информацию
            display_frame = self.draw_info(frame, filename)
            
            # Показываем
            cv2.imshow(window_name, display_frame)
            
            # Ждем нажатия клавиши
            key = cv2.waitKey(0) & 0xFF
            
            # Обработка команд
            if key == ord('q'):
                print("\n👋 Выход...")
                break
            
            elif key == ord('h'):
                self.print_help()
            
            elif key == ord('s'):
                print(f"⏭️  Пропущено: {filename}")
                self.current_idx += 1
            
            elif key == ord('b'):
                if self.current_idx > 0:
                    self.current_idx -= 1
                    print(f"⏪ Назад к кадру {self.current_idx + 1}")
                else:
                    print("⚠️  Уже первый кадр")
            
            elif key == ord('d'):
                if filename in self.labeled_data["annotations"]:
                    del self.labeled_data["annotations"][filename]
                    print(f"🗑️  Удалена метка для {filename}")
                else:
                    print(f"⚠️  {filename} не имеет метки")
            
            # Проверка цифр (метки)
            elif chr(key).isdigit():
                label_idx = int(chr(key)) - 1
                if 0 <= label_idx < len(self.labels):
                    selected_label = self.labels[label_idx]
                    
                    self.labeled_data["annotations"][filename] = {
                        "label": selected_label,
                        "frame_path": str(frame_path),
                        "labeled_at": datetime.now().isoformat()
                    }
                    
                    print(f"✓ {filename} -> {selected_label}")
                    self.current_idx += 1
                else:
                    print(f"⚠️  Недопустимая метка: {label_idx + 1}")
            
            else:
                print(f"⚠️  Неизвестная команда: {chr(key)}")
        
        cv2.destroyAllWindows()
        
        # Сохраняем
        self.save_labels()
        
        # Финальная статистика
        print("\n" + "="*60)
        print("ФИНАЛЬНАЯ СТАТИСТИКА:")
        print("="*60)
        stats = self.get_stats()
        total_labeled = sum(stats.values())
        
        for label, count in sorted(stats.items()):
            percentage = (count / total_labeled * 100) if total_labeled > 0 else 0
            print(f"  {label}: {count} ({percentage:.1f}%)")
        
        print(f"\nВсего размечено: {total_labeled}/{self.total_frames} "
              f"({total_labeled/self.total_frames*100:.1f}%)")
        print("="*60)


def main():
    parser = argparse.ArgumentParser(
        description="Интерактивный лейблер кадров для CNN",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:

1. Бинарная классификация:
   python frame_labeler.py frames -l "defect" "ok"

2. Многоклассовая классификация:
   python frame_labeler.py frames -l "cat" "dog" "bird" "other"

3. Продолжить с кадра 50:
   python frame_labeler.py frames -l "class1" "class2" --start 50

4. Свой файл для меток:
   python frame_labeler.py frames -l "good" "bad" -o my_labels.json
        """
    )
    
    parser.add_argument(
        "frames_dir",
        help="Директория с кадрами"
    )
    
    parser.add_argument(
        "-l", "--labels",
        nargs="+",
        required=True,
        help="Список меток (например: good bad unknown)"
    )
    
    parser.add_argument(
        "-o", "--output",
        default="labels.json",
        help="Файл для сохранения меток (по умолчанию: labels.json)"
    )
    
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="С какого кадра начать (для продолжения)"
    )
    
    args = parser.parse_args()
    
    try:
        labeler = FrameLabeler(
            frames_dir=args.frames_dir,
            labels=args.labels,
            output_json=args.output,
            start_from=args.start
        )
        labeler.run()
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
