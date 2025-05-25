import os
import shutil
from pathlib import Path

# 병합 대상 데이터셋들
source_datasets = [
    "E:/Chairs/Project_chairs1",
    "E:/Chairs/Project_chairs2",
    "E:/Chairs/Project_chairs3",
    "E:/Chairs/Project_chairs4",
    "E:/Chairs/Project_chairs5",
    "E:/Chairs/Project_chairs6"
]

# 병합될 최종 폴더
target_root = "E:/Chairs/Merged_Chairs_Dataset"

splits = ["train", "valid", "test"]
subdirs = ["images", "labels"]

# 1. 병합할 폴더 생성
for split in splits:
    for subdir in subdirs:
        path = Path(target_root) / split / subdir
        path.mkdir(parents=True, exist_ok=True)

# 2. 복사 시작 (중복 방지 위해 파일명 변경)
for dataset in source_datasets:
    for split in splits:
        for subdir in subdirs:
            src_dir = Path(dataset) / split / subdir
            dst_dir = Path(target_root) / split / subdir

            if not src_dir.exists():
                continue

            for file in src_dir.glob("*.*"):
                # 파일명에 원본 데이터셋명 붙이기 (중복 방지)
                new_name = f"{file.stem[:30]}_{Path(dataset).stem}{file.suffix}"
                new_path = dst_dir / new_name
                shutil.copy(file, new_path)

print("✅ 데이터셋 병합 완료")
