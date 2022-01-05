# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:\\BlueBox\\BlueBox_file\\Pycharm_Project\\20220105\\main.py'],
             pathex=['E:\\BlueBox\\BlueBox_file\\Pycharm_Project\\20220105\\image\\logo.jpg'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=["appdirs", "bcrypt", "certifi", "cryptography", "docutils", "IPython", "jedi", "jinja2",
              "jsonschema", "nacl", "nbconvert", "nbformat", "notebook", "parso", "pycparser","pytest", "difflib"
              "encodings", "importlib_metadata", "lib2to3", "multiprocessing", "numpy", "packaging"
              "regex"],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='MakeQrcode_BlueBox',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='E:\\BlueBox\\BlueBox_file\\Pycharm_Project\\20220105\\image\\logo.ico')
