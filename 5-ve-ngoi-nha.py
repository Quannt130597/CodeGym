from turtle import *
bgcolor ("green")
speed (0)

# Tô màu bãi cỏ
color ("green")

# Vẽ bầu trời
penup ()
goto (-400, -100)
pendown ()
color ("deepskyblue")
begin_fill ()

for i in range (2):
    forward (800)
    left (90)
    forward (500)
    left (90)
end_fill ()

# Vẽ mặt trời
penup ()
goto (-320, 225)
pendown ()
color ("orange", "yellow")
begin_fill ()
circle (35)
end_fill ()

# Vẽ mây
penup ()
goto (200, 200)
pendown ()
color ("white")
begin_fill ()
circle (25)
end_fill ()

penup ()
goto (220, 240)
pendown ()
color ("white")
begin_fill ()
circle (25)
end_fill ()

penup ()
goto (230, 215)
pendown ()
color ("white")
begin_fill ()
circle (25)
end_fill ()

penup ()
goto (180, 215)
pendown ()
color ("white")
begin_fill ()
circle (25)
end_fill ()

# Vẽ ngôi nhà
penup ()
goto (-100, -100)
pendown ()
pensize (3)
color ("brown", "orange")
begin_fill ()
for i in range (4):
    forward (170)
    left (90)
end_fill ()

# Mái nhà
penup ()
goto (20, 130)
pendown ()
color ("brown", "red")
begin_fill ()

for i in range (2):
    forward (40)
    left (90)
    forward (100)
    left (90)
end_fill ()

penup ()
goto (-127, 70)
pendown ()
begin_fill ()
for i in range (3):
    forward (225)
    left (120)
end_fill ()

# Vẽ cửa sổ
penup ()
goto (0, 0)
pendown ()
color ("black", "white")
begin_fill ()
for i in range (4):
    forward (50)
    left (90)
end_fill ()

# Vẽ cửa chính
penup ()
goto (-40, -20)
pendown ()
right (90)
color ("black", "white")
begin_fill ()
for i in range (2):
    forward (80)
    left (90)
    forward (50)
    left (90)
end_fill ()

mainloop ()