#!/usr/bin/env python3
"""
Скрипт для извлечения кадров из видео с настраиваемыми параметрами
для подготовки датасета для обучения CNN модели
"""

import cv2
import os
from pathlib import Path
import argparse


def extract_frames(
		video_path,
		output_dir,
		interval_seconds=1.0,
		skip_first_seconds=0,
		skip_last_seconds=0,
		max_frames=None,
		quality=95,
		resize_width=None,
		resize_height=None,
		show_preview=False
):
	"""
	Извлекает кадры из видео с заданным интервалом

	Параметры:
	-----------
	video_path : str
		Путь к видео файлу
	output_dir : str
		Директория для сохранения кадров
	interval_seconds : float
		Интервал между кадрами в секундах (по умолчанию 1.0)
	skip_first_seconds : float
		Пропустить первые N секунд видео
	skip_last_seconds : float
		Пропустить последние N секунд видео
	max_frames : int
		Максимальное количество кадров для извлечения (None = без ограничений)
	quality : int
		Качество JPEG (0-100, по умолчанию 95)
	resize_width : int
		Ширина для ресайза (None = оригинал)
	resize_height : int
		Высота для ресайза (None = оригинал)
	show_preview : bool
		Показывать превью каждого кадра
	"""
	
	# Создаем выходную директорию
	output_path = Path(output_dir)
	output_path.mkdir(parents=True, exist_ok=True)
	
	# Открываем видео
	cap = cv2.VideoCapture(video_path)
	
	if not cap.isOpened():
		raise ValueError(f"Не удалось открыть видео: {video_path}")
	
	# Получаем информацию о видео
	fps = cap.get(cv2.CAP_PROP_FPS)
	total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	duration = total_frames / fps
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	
	print(f"\n{'=' * 60}")
	print(f"Информация о видео:")
	print(f"{'=' * 60}")
	print(f"Разрешение: {width}x{height}")
	print(f"FPS: {fps:.2f}")
	print(f"Всего кадров: {total_frames}")
	print(f"Длительность: {duration:.2f} сек ({duration / 60:.2f} мин)")
	print(f"{'=' * 60}\n")
	
	# Вычисляем рабочий диапазон
	start_frame = int(skip_first_seconds * fps)
	end_frame = total_frames - int(skip_last_seconds * fps)
	
	# Интервал в кадрах
	frame_interval = int(interval_seconds * fps)
	
	# Расчет ожидаемого количества кадров
	expected_frames = (end_frame - start_frame) // frame_interval
	if max_frames:
		expected_frames = min(expected_frames, max_frames)
	
	print(f"Параметры извлечения:")
	print(f"  Интервал: {interval_seconds} сек (каждый {frame_interval}-й кадр)")
	print(f"  Начало: {skip_first_seconds} сек (кадр {start_frame})")
	print(f"  Конец: {duration - skip_last_seconds:.2f} сек (кадр {end_frame})")
	print(f"  Ожидаемое кол-во кадров: ~{expected_frames}")
	if resize_width or resize_height:
		print(f"  Ресайз: {resize_width or 'авто'}x{resize_height or 'авто'}")
	print()
	
	# Извлекаем кадры
	frame_count = 0
	saved_count = 0
	
	print("Извлечение кадров...")
	print("-" * 60)
	
	while True:
		ret, frame = cap.read()
		
		if not ret:
			break
		
		# Проверяем диапазон
		if frame_count < start_frame:
			frame_count += 1
			continue
		
		if frame_count >= end_frame:
			break
		
		# Извлекаем каждый N-й кадр
		if (frame_count - start_frame) % frame_interval == 0:
			
			# Ресайз если нужно
			if resize_width or resize_height:
				if resize_width and resize_height:
					frame = cv2.resize(frame, (resize_width, resize_height))
				elif resize_width:
					ratio = resize_width / width
					new_height = int(height * ratio)
					frame = cv2.resize(frame, (resize_width, new_height))
				else:  # resize_height
					ratio = resize_height / height
					new_width = int(width * ratio)
					frame = cv2.resize(frame, (new_width, resize_height))
			
			# Формируем имя файла
			timestamp = frame_count / fps
			filename = f"frame_{saved_count:05d}_t{timestamp:.2f}s.jpg"
			filepath = output_path / filename
			
			# Сохраняем
			cv2.imwrite(str(filepath), frame, [cv2.IMWRITE_JPEG_QUALITY, quality])
			
			# Показываем превью если нужно
			if show_preview:
				cv2.imshow('Frame Preview', frame)
				cv2.waitKey(1)
			
			saved_count += 1
			
			# Прогресс
			if saved_count % 10 == 0:
				print(f"Сохранено: {saved_count} кадров | Время: {timestamp:.2f}s")
			
			# Проверяем максимум
			if max_frames and saved_count >= max_frames:
				print(f"\nДостигнут лимит: {max_frames} кадров")
				break
		
		frame_count += 1
	
	cap.release()
	if show_preview:
		cv2.destroyAllWindows()
	
	print("-" * 60)
	print(f"\n✓ Готово! Сохранено {saved_count} кадров в {output_dir}")
	
	# Статистика размера
	total_size = sum(f.stat().st_size for f in output_path.glob("*.jpg"))
	avg_size = total_size / saved_count if saved_count > 0 else 0
	print(f"  Общий размер: {total_size / (1024 * 1024):.2f} МБ")
	print(f"  Средний размер кадра: {avg_size / 1024:.2f} КБ")
	print()
	
	return saved_count


def main():
	parser = argparse.ArgumentParser(
		description="Извлечение кадров из видео для обучения CNN модели",
		formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog="""
Примеры использования:

1. Каждую секунду (233 кадра для 3:53 видео):
   python video_frame_extractor.py video.mp4 -i 1.0

2. Каждые 2 секунды (116 кадров):
   python video_frame_extractor.py video.mp4 -i 2.0

3. Каждые 0.5 секунды с пропуском начала и конца:
   python video_frame_extractor.py video.mp4 -i 0.5 --skip-start 5 --skip-end 5

4. Ограничить 200 кадрами с ресайзом:
   python video_frame_extractor.py video.mp4 -i 1.0 --max 200 --width 640

5. Показывать превью в процессе:
   python video_frame_extractor.py video.mp4 -i 1.0 --preview
        """
	)
	
	parser.add_argument(
		"video",
		help="Путь к видео файлу"
	)
	
	parser.add_argument(
		"-o", "--output",
		default="frames",
		help="Директория для кадров (по умолчанию: frames)"
	)
	
	parser.add_argument(
		"-i", "--interval",
		type=float,
		default=1.0,
		help="Интервал между кадрами в секундах (по умолчанию: 1.0)"
	)
	
	parser.add_argument(
		"--skip-start",
		type=float,
		default=0,
		help="Пропустить первые N секунд"
	)
	
	parser.add_argument(
		"--skip-end",
		type=float,
		default=0,
		help="Пропустить последние N секунд"
	)
	
	parser.add_argument(
		"--max",
		type=int,
		help="Максимальное количество кадров"
	)
	
	parser.add_argument(
		"-q", "--quality",
		type=int,
		default=95,
		help="Качество JPEG 0-100 (по умолчанию: 95)"
	)
	
	parser.add_argument(
		"--width",
		type=int,
		help="Ширина для ресайза (высота авто)"
	)
	
	parser.add_argument(
		"--height",
		type=int,
		help="Высота для ресайза (ширина авто)"
	)
	
	parser.add_argument(
		"--preview",
		action="store_true",
		help="Показывать превью кадров"
	)
	
	args = parser.parse_args()
	
	try:
		extract_frames(
			video_path=args.video,
			output_dir=args.output,
			interval_seconds=args.interval,
			skip_first_seconds=args.skip_start,
			skip_last_seconds=args.skip_end,
			max_frames=args.max,
			quality=args.quality,
			resize_width=args.width,
			resize_height=args.height,
			show_preview=args.preview
		)
	except Exception as e:
		print(f"\n❌ Ошибка: {e}")
		return 1
	
	return 0


if __name__ == "__main__":
	exit(main())