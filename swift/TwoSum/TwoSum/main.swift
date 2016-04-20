//
//  main.swift
//  TwoSum
//
//  Created by lan on 16-4-19.
//  Copyright (c) 2016年 alenslan. All rights reserved.
//  swift 2.0版本
//

class Solution {
    func twoSum(nums: [Int], _ target: Int) -> [Int] {
        var d = [Int: Int]()
        var r = [Int]()
        
        if (nums == []) {
            return r
        }
        
        for (index, item) in enumerate(nums) {
            if (d[target - item] != nil){
                var v = d[target - item]
                r.append(v!)
                r.append(index)
            } else {
                d[item] = index
            }
        }
        
        return r
    }
}
//
//
var soc = Solution()

var c = soc.twoSum([2, 7, 11, 15], 9)

print(c)

var d = soc.twoSum([3,2,4], 6)

print(d)
