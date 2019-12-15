# Ean
A Nix/NixOS wrapper with fast, intuitive command and awesome completion.

Ean basically rename and map `nix`, `nix-env`, `nix-channel`, and `nixos-rebuild`
commands, add completion, and create cache whenever it needs.

## Manual

**Package command**
```
search [-i|--installed] <pattern>
install [<channel>.]<package>
remove <package>
update [<channel>]
```

**Channel command**
```
channel update <channel>
channel remove <channel>
channel add <channel>
```

**NixOS command**
```
os rebuild
os list
os roll <generation>
```
