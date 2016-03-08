#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'zhen'


# -*- coding: utf-8 -*-

# ---- init some data ----
# 隐藏变量， states
states = ['h', 'f']

# 状态转移矩阵
Tr_p = {}
Tr_p['h'] = { 'h': 0.7, 'f': 0.3}
Tr_p['f'] = { 'h': 0.4, 'f': 0.6}

# 初始概率， star=*, 有的是用π来表示
star = {}
star['h'] = 0.6
star['f'] = 0.4

# 放射矩阵， n=normal, c=cold, d=dizzy
emission_p = {}
emission_p['h'] = { 'n' : 0.5, 'c' : 0.4, 'd':0.1 }
emission_p['f'] = { 'n' : 0.1, 'c' : 0.3, 'd':0.6 }


# 实际的观察值
obser_vals = ['n', 'c', 'd']


def get_max_from_dict(delta) :
	max_val = 0
	max_key = ""

	for key in delta.keys() :
		if delta[key] > max_val :
			max_key = key
			max_val = delta[key]

	return max_key, max_val
def viterbi() :
	# delta 用于保存当前状态下
	delta_i = {}
	path_i = []
	prob_i = []
	# 首先计算第一天的状态
	# delta_i['h'] = star['h'] * emission_p['h']['n']
	# delta_i['f'] = star['f'] * emission_p['f']['n']
	for state in states :
		delta_i[state] = star[state] * emission_p[state][obser_vals[0]]


	key, val = get_max_from_dict(delta_i)
	path_i.append(key)
	prob_i.append(val)
	# 从第二天开始计算，直到最后一天
	for i in range(1, len(obser_vals)) :
		lastState = path_i[-1]
		obser_val = obser_vals[i]

		# 防止出错，清空delta_i
		delta_i = {}
		for state in states :
			# Δ2(h)        = Δ1(h)      * Tr(h->h)               * e(h | c)
			delta_i[state] = prob_i[-1] * Tr_p[lastState][state] * emission_p[state][obser_val]
			print "delta_i[state]=", delta_i[state]

		# 获取当前概率最大的路径
		key, val = get_max_from_dict(delta_i)
		path_i.append(key)
		prob_i.append(val)

	print path_i

viterbi()
