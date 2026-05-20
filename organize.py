#!/usr/bin/env python3
"""Organize files in a directory by extension."""
import sys, os, shutil, argparse
from pathlib import Path

CATEGORIES = {
    "Images":     {".jpg",".jpeg",".png",".gif",".webp",".svg",".bmp",".ico"},
    "Videos":     {".mp4",".mov",".avi",".mkv",".webm",".flv"},
    "Audio":      {".mp3",".wav",".flac",".aac",".ogg",".m4a"},
    "Documents":  {".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".txt",".md"},
    "Archives":   {".zip",".tar",".gz",".rar",".7z",".bz2"},
    "Code":       {".py",".js",".ts",".html",".css",".go",".rs",".java",".cpp",".c",".sh"},
    "Data":       {".json",".csv",".xml",".yaml",".yml",".sql"},
}

def category(ext):
    for cat, exts in CATEGORIES.items():
        if ext.lower() in exts: return cat
    return "Others"

def organize(folder, dry_run=False):
    folder = Path(folder)
    moved = 0
    for f in folder.iterdir():
        if not f.is_file(): continue
        cat = category(f.suffix)
        dest = folder / cat / f.name
        print(f"  {'[DRY]' if dry_run else ''} {f.name} → {cat}/")
        if not dry_run:
            (folder / cat).mkdir(exist_ok=True)
            shutil.move(str(f), str(dest))
        moved += 1
    print(f"\n{'Would move' if dry_run else 'Moved'} {moved} files.")

p = argparse.ArgumentParser()
p.add_argument("folder")
p.add_argument("--dry-run", action="store_true")
args = p.parse_args()
organize(args.folder, args.dry_run)
