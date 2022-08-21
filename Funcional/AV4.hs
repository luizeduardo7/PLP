removevogal [] = []
removevogal (p:ps) | elem p "aeiouAEIOU" = removevogal ps
                   | otherwise = p:(removevogal ps)
tamanho ps = sum [1 | _ <- ps] 
replaces palavra = (removevogal palavra, tamanho palavra, tamanho(removevogal palavra))


