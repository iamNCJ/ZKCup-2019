@echo off
set a=00
setlocal EnableDelayedExpansion
for %%n in (*.jpg) do (
set /A a+=1
ren "%%n" "data_!a!.jpg"
)
for %%n in (*.png) do (
set /A a+=1
ren "%%n" "data_!a!.png"
)
for %%n in (*.bmp) do (
set /A a+=1
ren "%%n" "data_!a!.bmp"
)
for %%n in (*.gif) do (
set /A a+=1
ren "%%n" "data_!a!.gif"
)
for %%n in (*.jpeg) do (
set /A a+=1
ren "%%n" "data_!a!.jpeg"
)
