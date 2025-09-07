main :: IO ()
main = do
    let n = 5
    mapM_ putStrLn (pyramid n)

pyramid :: Int -> [String]
pyramid n = [ line i | i <- [1..n] ]
  where
    line i
      | i == 1    = replicate (n - i) ' ' ++ "*"
      | i == n    = replicate (2 * n - 1) '*'
      | otherwise = replicate (n - i) ' ' ++ "*" ++ replicate (2 * i - 3) ' ' ++ "*"
