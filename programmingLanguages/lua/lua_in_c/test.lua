a = 10
b = 50
local b = 30
for i = 1, 10, 1 do
    print(i^2)
end
c = 3.14
s = "this is a string defined in Lua script."

function radius(x, y)
    return math.sqrt(x^2 + y^2)
end

function decimal(x,y,z,s)
    return x * 100 + y * 10 + z .. s
end
