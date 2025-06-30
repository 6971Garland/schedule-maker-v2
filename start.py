#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
排班表制作器启动脚本
"""

import sys
import os

def main():
    print("=== 智能排班表制作器 V2 ===")
    print("正在启动排班算法...")
    
    try:
        # 导入并运行核心排班脚本
        import subprocess
        result = subprocess.run([sys.executable, '最终优化排班脚本.py'], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("\n✅ 排班表生成成功！")
            print("\n生成的文件:")
            print("- 最终优化七月排班表.xlsx")
            print("- 最终优化排班数据.json")
            print("\n" + result.stdout)
        else:
            print("❌ 排班表生成失败！")
            print("错误信息:", result.stderr)
            
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())