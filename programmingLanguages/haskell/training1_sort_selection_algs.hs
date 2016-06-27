{-- This is just my sandbox to learn haskell. --}

import Data.Maybe {-- fromJust --}
import Debug.Trace {-- trace --}


remove' :: Int -> [a] -> [a]
remove' n xs = take n xs ++ drop (n + 1) xs


sorting :: Ord a => [a] -> [a]
sorting [] = []
sorting (xs) = lt ++ [x] ++ gt
	where
	 c = length (xs) `div` 2
	 x = xs !! c
	 ys = remove' c xs
	 gt = sorting [y|y <- ys, y >= x]
	 lt = sorting [y|y <- ys, y < x]

{-- quick select algorithm --}
selection :: (Show a, Ord a) => Int -> [a] -> Maybe a
selection _ []  = Nothing
selection _ [z] = Just z
selection n (xs)
	| len_g == n - 1 = Just x
	| len_g > n - 1 = selection (n) gt
	| len_g < n - 1 = selection (n - len_g - 1) lt
	where 
	 c = length (xs) `div` 2
	 x = xs !! c
	 ys = remove' c xs
	 gt = [y|y <- ys, y >= x]
	 lt = [y|y <- ys, y <  x]
	 len_g = trace (show n ++ ":" ++ show lt ++ show [x] ++ show gt) length (gt)


main :: IO()
main = do
	let s = [35,1,7,32,5,54,2,54,67,87,85,43,312,24,356,648,87,87,87,87,204,4,10,14]
	print . sorting $ s
	print . fromJust . (selection 1) $ s
	print . fromJust . (selection 5) $ s
	print . fromJust . (selection 15) $ s
	print . fromJust . (selection 10) $ [100,90..1] ++ [2..40]
