{
  'includes': [ '../common.gyp' ],
  'targets': [
    {
      'target_name': 'zlib',
      'type': 'static_library',
      'defines': [
      ],
      'include_dirs': [
        '.'
      ],
      'sources': [
        'adler32.c',
        'compress.c',
        'crc32.c',
        'deflate.c',
        'gzclose.c',
        'gzlib.c',
        'gzread.c',
        'gzwrite.c',
        'infback.c',
        'inffast.c',
        'inflate.c',
        'inftrees.c',
        'trees.c',
        'uncompr.c',
        'zutil.c',
      ],
    },
  ]
}
