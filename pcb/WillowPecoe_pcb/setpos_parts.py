
# 

import pcbnew

OFFSET_X = 0.0
OFFSET_Y = 0.0

pcb = pcbnew.GetBoard()

def set_footprint_position(name, xp, yp, rot):
    module = pcb.FindModuleByReference(name)
    module.SetPosition(pcbnew.wxPointMM(xp  + OFFSET_X, yp + OFFSET_Y))
    module.SetOrientationDegrees(rot)  


parts = [
('SW1', 	-137.864, 	28.321,	358.88),
('SW2', 	-139.387, 	48.354,	-7.57),
('SW3', 	-143.235, 	68.138,	-14.39),
('SW4', 	-118.68, 	26.959,	359.71),
('SW5', 	-119.881, 	46.979,	-6.55),
('SW6', 	-122.929, 	66.493,	-10.85),
('SW7', 	-99.483, 	22.671,	1.06),
('SW8', 	-100.099, 	42.625,	355.42),
('SW9', 	-102.759, 	62.481,	-10.66),
('SW10', 	-80.381, 	15.87,	1.98),
('SW12', 	-82.065, 	55.46,	-7.62),
('SW11', 	-80.388, 	35.574,	-2.02),
('SW13', 	-85.723, 	75.12,	346.53),
('SW14', 	-61.117, 	21.376,	362.05),
('SW15', 	-60.887, 	41.351,	356.38),
('SW16', 	-63.482, 	61.083,	-8.51),
('SW17', 	-67.373, 	80.64,	-14),
('SW18', 	-41.814, 	33.577,	-2.02),
('SW19', 	-43.088, 	53.145,	-5.43),
('SW20', 	-45.956, 	72.904,	348.92),
('SW21', 	-51.041, 	94.399,	-105.12),
('SW22', 	-27.523, 	77.875,	-11.13),
('SW23', 	-32.651, 	99.366,	74.89),
('SW24', 	0, 	103.819,	0),
('SW25', 	27.488, 	77.819,	-348.87),
('SW26', 	32.616, 	99.309,	-74.89),
('SW27', 	41.779, 	33.52,	2.02),
('SW28', 	43.053, 	53.088,	5.43),
('SW29', 	45.92, 	72.848,	11.08),
('SW30', 	51.006, 	94.342,	105.12),
('SW31', 	61.082, 	21.32,	-2.05),
('SW32', 	61.352, 	41.294,	3.62),
('SW33', 	63.447, 	61.026,	8.51),
('SW34', 	67.337, 	80.583,	14),
('SW35', 	80.346, 	15.813,	-1.98),
('SW36', 	80.353, 	35.517,	2.02),
('SW37', 	82.029, 	55.403,	7.62),
('SW38', 	85.688, 	75.063,	13.47),
('SW39', 	99.448, 	22.614,	-1.06),
('SW40', 	100.063, 	42.569,	4.58),
('SW41', 	102.724, 	62.425,	10.66),
('SW42', 	118.645, 	26.902,	0.28),
('SW44', 	122.893, 	66.437,	10.85),
('SW43', 	119.846, 	46.922,	6.55),
('SW45', 	137.828, 	28.264,	1.12),
('SW46', 	139.351, 	48.298,	7.57),
('SW47', 	143.2, 	68.081,	14.39),
('SW48', 	157.498, 	34.238,	4.17),
('SW49', 	159.981, 	54.296,	10.66),
('RE1', 	-165.678, 	60.38,	-7.6),
('ProMicro1', 	-159.824, 	36.706,	-7.6),
('RSTSW1', 	-173.422, 	37.165,	-97.6),
('LED1', 	-117.372, 	13.954,	-172.38),
('LED2', 	-40, 	10.412,	180),
('LED3', 	-18.406, 	15.157,	180),
('LED4', 	0.017, 	15.157,	-180),
('LED5', 	18.44, 	15.157,	-180),
('LED6', 	40, 	10.412,	180),
('LED7', 	114.783, 	13.954,	-187.62),
('LED8', 	166.4, 	70.834,	15.12),
('LED9', 	115.507, 	83.092,	15.12),
('LED10', 	74.786, 	93.352,	15.12),
('LED11', 	18.988, 	106.426,	0),
('LED12', 	-18.988, 	106.426,	0),
('LED13', 	-74.785, 	93.352,	344.89),
('LED14', 	-115.507, 	83.092,	344.89),
('LED15', 	-166.399, 	70.834,	344.89),
			
('LED16', 	-117.372, 	13.954,	-172.38),
('LED17', 	-40, 	10.412,	180),
('LED18', 	-18.406, 	15.157,	180),
('LED19', 	0.017, 	15.157,	-180),
('LED20', 	18.44, 	15.157,	-180),
('LED21', 	40, 	10.412,	180),
('LED22', 	114.783, 	13.954,	-187.62),
('LED23', 	166.4, 	70.834,	15.12),
('LED24', 	115.507, 	83.092,	15.12),
('LED25', 	74.786, 	93.352,	15.12),
('LED26', 	18.988, 	106.426,	0),
('LED27', 	-18.988, 	106.426,	0),
('LED28', 	-74.785, 	93.352,	344.89),
('LED29', 	-115.507, 	83.092,	344.89),
('LED30', 	-166.399, 	70.834,	344.89),

('D1',  	-134.702, 	20.081,	358.88),
('D2',  	-135.319, 	40.522,	-7.57),
('D3',  	-138.266, 	60.844,	-14.39),
('D4',  	-115.639, 	18.674,	359.71),
('D5',  	-115.954, 	39.075,	-6.55),
('D6',  	-118.42, 	58.906,	-10.85),
('D7',  	-96.637, 	14.317,	1.06),
('D8',  	-96.445, 	34.592,	355.42),
('D9',  	-98.275, 	54.88,	-10.66),
('D10',  	-77.669, 	7.471,	1.98),
('D12',  	-77.991, 	47.631,	-7.62),
('D11',  	-77.097, 	27.385,	-2.02),
('D13',  	-80.872, 	67.747,	346.53),
('D14',  	-58.417, 	12.974,	362.05),
('D15',  	-57.368, 	33.257,	356.38),
('D16',  	-59.287, 	53.318,	-8.51),
('D17',  	-62.454, 	73.312,	-14),
('D18',  	-38.523, 	25.388,	-2.02),
('D19',  	-39.317, 	45.166,	-5.43),
('D20',  	-41.416, 	65.336,	348.92),
('D21',  	-43.811, 	99.459,	-105.12),
('D22',  	-22.978, 	70.31,	-11.13),
('D23',  	-39.882, 	94.305,	74.89),
('D24',  	3, 	95.519,	0),
('D25',  	28.83, 	69.096,	-348.87),
('D26',  	41.411, 	100.041,	-74.89),
('D27',  	44.484, 	25.12,	2.02),
('D28',  	45.254, 	44.542,	5.43),
('D29',  	47.269, 	64.126,	11.08),
('D30',  	42.211, 	93.61,	105.12),
('D31',  	64.378, 	13.133,	-2.05),
('D32',  	63.821, 	32.821,	3.62),
('D33',  	65.186, 	52.374,	8.51),
('D34',  	68.241, 	71.804,	14),
('D35',  	83.631, 	7.622,	-1.98),
('D36',  	83.058, 	27.116,	2.02),
('D37',  	83.903, 	46.778,	7.62),
('D38',  	86.672, 	66.293,	13.47),
('D39',  	102.601, 	14.371,	-1.06),
('D40',  	102.39, 	34.056,	4.58),
('D41',  	104.136, 	53.713,	10.66),
('D42',  	121.604, 	18.587,	0.28),
('D44',  	124.277, 	57.72,	10.85),
('D43',  	121.88, 	38.334,	6.55),
('D45',  	140.665, 	19.907,	1.12),
('D46',  	141.232, 	39.675,	7.57),
('D47',  	144.042, 	59.296,	14.39),
('D48',  	159.887, 	25.742,	4.17),
('D49',  	161.393, 	45.584,	10.66),
('DRE1',  	-162.678, 	52.08,	-7.6),

]

for p in parts:
    set_footprint_position(p[0], p[1], p[2], p[3])

