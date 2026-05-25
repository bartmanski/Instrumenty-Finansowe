#!/usr/bin/env python3
"""
Setup script to create and configure virtual environment for Jupyter notebook.
Reads settings from settings.txt and supports both venv and uv.
"""

import os
import sys
import subprocess
import configparser
from pathlib import Path

def read_settings(settings_file):
    """Read settings from settings.txt"""
    config = configparser.ConfigParser()
    config.read(settings_file)
    return config

def create_venv_with_uv(venv_path, python_version, dependencies):
    """Create virtual environment using uv"""
    print(f"📦 Creating virtual environment with uv: {venv_path}")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "uv"], check=False)
        cmd = ["uv", "venv", str(venv_path), "--python", python_version]
        subprocess.run(cmd, check=True)
        
        # Install dependencies with uv
        activate_script = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / "activate"
        for dep in dependencies:
            if dep.strip():
                subprocess.run([str(venv_path / ("Scripts" if sys.platform == "win32" else "bin") / ("pip" if sys.platform == "win32" else "pip")), "install", dep.strip()], check=True)
        print(f"✓ Virtual environment created with uv")
        return True
    except Exception as e:
        print(f"✗ Failed to create venv with uv: {e}")
        return False

def create_venv_standard(venv_path, dependencies):
    """Create virtual environment using standard venv"""
    print(f"📦 Creating virtual environment: {venv_path}")
    try:
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
        
        # Install dependencies
        pip_path = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / ("pip.exe" if sys.platform == "win32" else "pip")
        for dep in dependencies:
            if dep.strip():
                subprocess.run([str(pip_path), "install", dep.strip()], check=True)
        print(f"✓ Virtual environment created")
        return True
    except Exception as e:
        print(f"✗ Failed to create venv: {e}")
        return False

def register_kernel(venv_path, kernel_name, display_name):
    """Register Jupyter kernel"""
    print(f"📝 Registering Jupyter kernel: {kernel_name}")
    try:
        pip_path = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / ("pip.exe" if sys.platform == "win32" else "pip")
        subprocess.run([str(pip_path), "install", "ipykernel"], check=True)
        
        python_path = venv_path / ("Scripts" if sys.platform == "win32" else "bin") / ("python.exe" if sys.platform == "win32" else "python")
        subprocess.run([
            str(python_path), "-m", "ipykernel", "install",
            "--user", "--name", kernel_name, "--display-name", display_name
        ], check=True)
        print(f"✓ Kernel registered: {display_name}")
        return True
    except Exception as e:
        print(f"✗ Failed to register kernel: {e}")
        return False

def main():
    script_dir = Path(__file__).parent
    settings_file = script_dir / "settings.txt"
    
    if not settings_file.exists():
        print(f"✗ settings.txt not found in {script_dir}")
        return 1
    
    config = read_settings(settings_file)
    
    # Read settings
    venv_name = config.get("project", "venv_name", fallback=".venv")
    venv_path = script_dir / venv_name
    python_version = config.get("project", "python_version", fallback="3.11")
    
    # Parse dependencies
    dependencies = [
        d.strip() for d in config.get("dependencies", None, fallback="").split("\n")
    ]
    dependencies = [d for d in dependencies if d]
    
    kernel_name = config.get("jupyter", "kernel_name", fallback="projekt-env")
    display_name = config.get("jupyter", "display_name", fallback="Projekt Environment")
    
    print("=" * 60)
    print("🚀 Setting up Jupyter environment")
    print("=" * 60)
    
    # Try uv first, fall back to venv
    use_uv = "--uv" in sys.argv
    
    if use_uv:
        if not create_venv_with_uv(venv_path, python_version, dependencies):
            print("\n⚠️  uv failed, falling back to standard venv...")
            create_venv_standard(venv_path, dependencies)
    else:
        create_venv_standard(venv_path, dependencies)
    
    # Register kernel
    register_kernel(venv_path, kernel_name, display_name)
    
    print("\n" + "=" * 60)
    print("✨ Setup complete!")
    print(f"📍 Virtual environment: {venv_path}")
    print(f"📓 Jupyter kernel: {kernel_name}")
    print(f"💡 To use in VS Code, select '{display_name}' as the kernel")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
