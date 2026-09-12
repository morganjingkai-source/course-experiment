# 定义目标文件
STATS = stats.txt
REPORT = report.txt
DATA = data.csv
SCRIPT_STATS = stats.py
SCRIPT_REPORT = build_report.py
SOURCE_REPORT = report.md

# 默认目标
all: $(STATS) $(REPORT)

# 生成 stats.txt
$(STATS): $(DATA) $(SCRIPT_STATS)
	python3 $(SCRIPT_STATS)

# 生成 report.txt
$(REPORT): $(SOURCE_REPORT) $(STATS) $(SCRIPT_REPORT)
	python3 $(SCRIPT_REPORT)

# 清理生成物
clean:
	rm -f $(STATS) $(REPORT)

# 声明伪目标
.PHONY: all clean
