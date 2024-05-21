#!/usr/bin/python3
"""Initializes from the package  FileStorage"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
