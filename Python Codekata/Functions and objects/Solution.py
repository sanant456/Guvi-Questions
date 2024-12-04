class Testcase:
  def __init__(self,n,x,a):
    self.n = n
    self.x = x
    self.a = a
    
  def calculate_qualified_elements(self):
    a_sorted = sorted(self.a, reverse = true)
    p,q = 0, 0
    #....YOUR CODE STARTS HERE....

  for i in range(len(a_sorted)):
    p += a_sorted[i]
            if p/(i+1) >= self.x:
                q += 1

    #....YOUR CODES ENDS HERE....
    return q

def process_test_cases():
  test_cases = int(input())
  results = []

  for _ in range(test_cases):
    n, x = map(int, input().spilt())
    a = list(map(int, input().spilt()))

  #....YOUR CODE STARTS HERE....
 test_case = TestCase(n,x,a)
        qualified_elements = test_case.calculate_qualified_elements()
        results.append(qualified_elements)
 
  #....YOUR CODES ENDS HERE....

return results


if __name__ = "__main__":
  results = process_test_cases()
  for result in results:
    print(result)


    
            
