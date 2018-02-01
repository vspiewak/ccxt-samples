from multiprocessing import Pool
import time

def getMarketDatas():
    time.sleep(1)
    print("Fetched All datas")

print("in serial !")
solve()
solve()
solve()
solve()
solve()
solve()
solve()
solve()
solve()
solve()


print("in parallel !")

pool = Pool()
result1 = pool.apply_async(solve)    # evaluate "solve1(A)" asynchronously
result2 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously
result3 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously
result4 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously
result5 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously
result6 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously
result7 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously
result8 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously
result9 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously
result10 = pool.apply_async(solve)    # evaluate "solve2(B)" asynchronously

answer1 = result1.get(timeout=10)
answer2 = result2.get(timeout=10)
answer3 = result3.get(timeout=10)
answer4 = result4.get(timeout=10)
answer5 = result5.get(timeout=10)
answer6 = result5.get(timeout=10)
answer7 = result5.get(timeout=10)
answer8 = result5.get(timeout=10)
answer9 = result5.get(timeout=10)
answer10 = result5.get(timeout=10)
