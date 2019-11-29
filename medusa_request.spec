# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['medusa_request.py', 'public\\common_util.py', 'public\\excel2case.py',
'public\\html_test_runner_api.py', 'public\\read_config.py', 'public\\request2result.py',
'public\\test_execute.py', 'public\\unittest_ddt_api.py'],
             pathex=['D:\\CodeSpace\\GitProject\\Medusa'],
             binaries=[],
             datas=[],
             hiddenimports=[''],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
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
          name='medusa_request',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
