n = 5  

for i in 1..n
  spaces = " " * (n - i)
  if i == 1
    puts spaces + "*"
  elsif i == n
    puts "*" * (2 * n - 1)
  else
    inner_spaces = " " * (2 * i - 3)
    puts spaces + "*" + inner_spaces + "*"
  end
end
