import logging
from typing import Tuple

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class MyBigNumber:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def sum(self, number1:str, number2:str) -> str:
        self.logger.info(f"Bắt đầu cộng hai số:")

        res = []
        carry = 0
        i = len(number1) - 1
        j = len(number2) - 1

        while i >= 0 or j >= 0 or carry:
            digit1 = int(number1[i]) if i >= 0 else 0
            digit2 = int(number2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            res.append(str(total % 10))

            self.logger.info(f"Lấy {digit1} cộng {digit2} được kết quả là {total}, nhớ là {carry}")

            i -= 1
            j -= 1
            final_res = ''.join(reversed(res))
        
        self.logger.info(f"Kết quả cuối cùng là: {final_res}")
        return final_res
    
# demo 
if __name__ == "__main__":
    bn = MyBigNumber()
    
    print("MyBigNumber - Addition Demo")
    print("-" * 60)
    
    test_cases = [
        ("12345678901234567890", "98765432109876543210"),
        ("99999999999999999999", "1"),
        ("0", "0"),
        ("500", "500"),
        ("123456789", "987654321"),
    ]
    
    for num1, num2 in test_cases:
        result = bn.sum(num1, num2)
        print(f"\n{num1} + {num2} = {result}")
        print("-" * 60)