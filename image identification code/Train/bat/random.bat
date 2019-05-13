@echo off
setlocal EnableDelayedExpansion
for %%n in (*.jpg) do (
ren "%%n" "!random!.jpg"
)
for %%n in (*.png) do (
ren "%%n" "!random!.png"
)
for %%n in (*.bmp) do (
ren "%%n" "!random!.bmp"
)
for %%n in (*.gif) do (
ren "%%n" "!random!.gif"
)
for %%n in (*.jpeg) do (
ren "%%n" "!random!.jpeg"
)
