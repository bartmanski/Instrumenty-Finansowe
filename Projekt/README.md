# Instrumenty Finansowe - Projekt

## 📋 Setup Instructions

This project uses a `settings.txt` configuration file to manage the Python virtual environment and Jupyter kernel setup.

### Quick Start

**Windows:**
```bash
setup.bat
```

**Linux/Mac:**
```bash
bash setup.sh
```

**Or manually with Python:**
```bash
python setup.py
```

### Using with `uv` (Faster)

If you have `uv` installed, use:
```bash
python setup.py --uv
```

Or:
```bash
setup.bat --uv
```

### Configuration

All settings are in `settings.txt`:
- **Python version**: Configure required Python version
- **Dependencies**: List your required packages
- **Jupyter kernel**: Customize kernel name and display name

### What the setup does:

1. ✅ Creates a Python virtual environment (`.venv`)
2. ✅ Installs all dependencies from `settings.txt`
3. ✅ Registers a Jupyter kernel connected to the venv
4. ✅ Notebook automatically uses this kernel

### After Setup

In VS Code:
1. Open `projekt.ipynb`
2. Select kernel → Choose **"Projekt Environment"**
3. Start coding! 🚀

### Adding Dependencies

1. Edit `settings.txt` and add packages under `[dependencies]`
2. Rerun `setup.bat` or `setup.sh` to install them

### Troubleshooting

If the kernel doesn't appear in VS Code:
- Reload the window: `Ctrl+Shift+P` → "Developer: Reload Window"
- Or manually select the interpreter path: `.venv/Scripts/python.exe` (Windows)
