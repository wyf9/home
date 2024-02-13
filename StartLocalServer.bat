@echo off
@set pypath=%1
@set port=%2
@%pypath% -m http.server %port%