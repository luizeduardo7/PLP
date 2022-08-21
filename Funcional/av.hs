
removeVogais [] = []
removeVogais (x:xs) | elem x "aeiouAEIOU" = removeVogais xs
                    | otherwise = x:(removeVogais xs)