def longestCommonSubsequence(text1: str, text2: str) -> int:
        text = [(a, i) for a, i in enumerate(text2)]
        count = 0
        
        if any(text[]) in text1:
            count+=1
            for i in range(0, len(text) - 1):
                if text[i+1] in text1.split(text[i])[1]:
                    count+=1
                    
                print(count)

        return count

def main():
    longestCommonSubsequence('bl', 'yby')

if __name__ == '__main__':
    main()
