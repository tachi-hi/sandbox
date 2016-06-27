

--  print
print("version: " .. _VERSION)
print (1 + 2)


-- for
local s = 0 -- variable without "local" is global
for i = 0, 10, 1 do
    --[[
    this measn
        for (i = 0; i <= 10; ++i)
    not
        for (i = 0; i != 10; ++i)
    ]]
    s = s + i
    -- "s += i" does not work
    print (i .. "th iteration: " .. s) -- ".." is string concatenation
end

-- array (hash table)
local s_ = {} -- init table
for i = 0, 10, 1 do
    s_[i] = i^3.01-- ^ is exp. ** does not work
    -- "s += i" does not work
    print (i .. "th iteration: " .. s_[i]) -- ".." is string concatenation.
end

-- access to elements
s_["hoge"] = "this is a string"
s_["123"] = "this is also a string"
s_["abc123"] = "this is an awesome string"
print(s_)
print(s_.hoge)
-- print(s_.3) --- it does not work
-- print(s_.123) -- no
print(s_.abc123) -- it works
print(s_[3])
print(s_[123]) -- nil
print(s_["123"])
print(s_["3"]) -- nil
s_["3"] = "homu"
print(s_[3]) -- 3
print(s_['3']) -- homu

-- iterator
for i, v in ipairs(s_) do -- numerical order
    print(i .. ' ' .. v)
end

for i, v in pairs(s_) do -- unspecified order
    print(i .. ' ' .. v)
end

-- function definition
function myfunc (x)
    return x + 100
end
print (myfunc(1))

-- lambda
local lmb = function(x) return x^2 end

print (lmb(1))

-- " cond ? val1 : val2 " -> cond and val1 or val2
myabs = function(x) return x >= 0 and x or -x end
for i = -10, 10, 1 do
    print(myabs(i))
end


--[[
f = io.input( "data.csv" )
for line in f:lines() do
    print (line)
end
]]--
