n =5

for i <- 1..n do
  spaces = String.duplicate(" ", n - i)

  cond do
    i == 1 ->
      IO.puts(spaces <> "*")

    i == n ->
      IO.puts(String.duplicate("*", 2 * n - 1))

    true ->
      inner_spaces = String.duplicate(" ", 2 * i - 3)
      IO.puts(spaces <> "*" <> inner_spaces <> "*")
  end
end
