{
  "targets": [
    {
      "target_name": "addon",
      "sources": [ "addon.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "cflags": [
        "<!@(pkg-config opencv4 --cflags)"
      ],
      "libraries": [
        "<!@(pkg-config opencv4 --libs)"
      ]
    }
  ]
}
