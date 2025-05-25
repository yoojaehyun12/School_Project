import os
from pathlib import Path


replace_map = {
    1: 3
    # 0: 0
}
# 경로 설정
label_dirs = ['E:/Chairs/Project_chairs6/test/labels', 
              'E:/Chairs/Project_chairs6/train/labels', 
              "E:/Chairs/Project_chairs6/val/labels"]
# found_class_ids = set()

for label_dir in label_dirs:
    # print(f"폴더: {label_dir}")

    if not os.path.exists(label_dir):
        print("경로 없음")
        continue
    print(f"처리 중: {label_dir}")
    for fname in os.listdir(label_dir):
        if not fname.endswith(".txt"):
            continue
        fpath = os.path.join(label_dir, fname)

        new_lines = []
        with open(fpath, "r") as f:
            for line in f:
                if line.strip() == '':
                    continue
                parts = line.strip().split()
                original_class_id = int(parts[0])

                new_class_id = replace_map.get(original_class_id, original_class_id)
                parts[0] = str(new_class_id)
                new_lines.append(" ".join(parts))
        
        # 파일 덮어쓰기
        with open(fpath, "w") as f:
            f.write("\n".join(new_lines) + "\n")

print("클래스 Id 변경 완료")
            # class_id = int(parts[0])
            # found_class_ids.add(class_id)
            # print(f"{fname} -> class ID : {class_id}")
#             break

# print("사용된 클래스 ID 목록: ", sorted(found_class_ids))
