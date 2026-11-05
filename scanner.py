#!/usr/bin/env python3
import os
import re
import json

def scan_project(root_dir="."):
    summary = {
        "underground": [],
        "walls": [],
        "keep": [],
        "watchtower": [],
        "risks": []
    }
    
    ignore_dirs = {".git", "node_modules", "__pycache__", ".venv", "dist", "build"}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for f in filenames:
            rel_path = os.path.relpath(os.path.join(dirpath, f), root_dir)
            ext = os.path.splitext(f)[1].lower()
            lower_name = f.lower()
            
            # 1. 지하 기초 (DB, Core, Env, Models)
            if (lower_name.endswith(('.sql', '.prisma')) or
                'migration' in rel_path.lower() or
                'model' in rel_path.lower() or
                lower_name in ['.env.example', 'docker-compose.yml']):
                summary["underground"].append(rel_path)
                
            # 2. 외벽 및 성문 (Auth, Router, API, Middleware)
            elif ('auth' in rel_path.lower() or
                  'middleware' in rel_path.lower() or
                  'router' in rel_path.lower() or
                  'gateway' in rel_path.lower()):
                summary["walls"].append(rel_path)
                
            # 3. 상층 망루 (UI, Components, Pages)
            elif (ext in ['.jsx', '.tsx', '.vue', '.svelte', '.html', '.css'] or
                  'component' in rel_path.lower() or
                  'page' in rel_path.lower() or
                  'view' in rel_path.lower()):
                summary["watchtower"].append(rel_path)
                
            # 4. 본관 내성 (Service, Logic, Utils)
            elif ext in ['.py', '.js', '.ts', '.go', '.java', '.rb']:
                summary["keep"].append(rel_path)

    # 기본 리스크 룰셋 검사
    if summary["watchtower"] and not summary["underground"]:
        summary["risks"].append("기초 부재: DB/코어 스키마 없이 상층 UI가 먼저 빌드되고 있습니다.")
    if summary["watchtower"] and not summary["walls"]:
        summary["risks"].append("성문 미비: 인증/보안 미들웨어 없이 화면 모듈이 노출되어 있습니다.")

    with open("castle_summary.json", "w", encoding="utf-8") as out:
        json.dump(summary, out, ensure_ascii=False, indent=2)

    return summary

if __name__ == "__main__":
    scan_project()
