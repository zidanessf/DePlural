import synonyms
def plural(new:str,ref:str):
    n0 = 6
    i = 0
    plural_count,plural_words_count = 0,0
    plural_lable = [0] * len(new)
    while i < len(new):
        if new[i:i+n0+1] in ref:
            plural_count += 1
            plural_words_count += n0
            k = 1
            i += n0
            for j in range(i,i+n0+1):
                plural_lable[j] = 1
            while new[i:i+n0+1+k] in ref:
                plural_words_count += 1
                i += 1
                k += 1
                plural_lable[i+n0+1+k] = 1
        else:
            i += 1
    return plural_count,plural_words_count,plural_lable
if __name__ == "__main__":
    ref = "风电出力受到复杂物理因素影响，并且其功率预测的不确定性难以被现有概率分布函数表征[15]。通过不确定集的方法，可以避免给出过于乐观的估计[16]。通过如公式(12)所示的盒式不确定集对每一时刻的风电出力预测误差进行建模。"
    new = "复杂的物理因素影响着风力发电量，现有的概率分布函数不能准确表示功率预测的不确定性[15]。通过使用不确定性集方法，可以避免过度乐观的估计[16]。可以通过方程(12)所示的区间不确定性模型来表征任意时刻的风功率预测误差："
    print(synonyms.seg(ref))