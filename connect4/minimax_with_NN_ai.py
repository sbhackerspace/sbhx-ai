from board import *
import random
import copy
import numpy

class MinimaxNNAI:

	def __init__(self, depth):
		self.depth = depth
		self.theta1 = numpy.matrix("""
			-0.024845, -0.095577, 0.001609, 0.149539, 0.087569, -0.177295, -0.041630, -0.068493, -0.334620, -0.084453, -0.459615, 0.141899, -0.241691, -0.223291, -0.027374, -0.212647, 0.073243, 0.106629, 0.790551, -0.212007, -0.198869, -0.636994, -0.047653, -0.103627, -0.215148, -0.268369, 0.236285, -0.099898, -0.684401, -0.102722, -0.151572, -0.136479, -0.240297, -0.276448, 0.360577, -0.543334, -0.127432, -0.119279, -0.988399, 0.783283, 0.812747, 1.186518, 2.254042;
			0.274847, -0.096838, -0.189608, -0.032534, 0.166880, -0.272383, -0.224304, 0.207344, 0.167724, -0.099855, -0.202930, 0.538745, -0.122978, -0.122839, -0.055563, 0.257353, -0.054239, -0.054077, -0.676076, -0.231272, -0.343527, -0.430106, 0.151657, 0.096874, -0.271197, 0.280798, -0.089089, 0.054365, -0.360230, 0.058765, -0.094253, -0.040399, 0.630505, 0.236393, 0.288486, -0.488673, 0.106479, 0.197338, 0.129534, 0.510368, 0.298715, 0.238121, -0.126251;
			-0.036894, 0.138475, -0.628325, 0.390600, 0.618632, 0.185569, 0.313968, 0.501792, -0.108114, 0.897933, -0.126769, 0.056439, 0.117012, -0.139630, 0.291704, -0.197216, -0.766319, -0.981343, 0.737014, -0.253527, -0.371985, 1.468681, -0.424075, -0.224418, 0.040840, -1.428809, -0.732253, -0.093670, 1.169559, -0.128214, 0.004647, -0.404860, -0.629341, -0.085185, -0.379098, 0.462418, 0.083103, -0.254387, -0.459661, 0.280454, 0.315343, 0.438987, 0.893240;
			-0.042617, 0.084464, 0.020473, 0.090037, 0.305865, 0.276333, -0.397006, -0.150389, 0.003116, 0.180064, 0.032436, -0.491223, -0.075071, -0.046230, -0.100295, -0.591409, -0.116252, -0.441595, -0.615729, -0.123878, -0.147725, -0.065250, -0.243461, -0.111889, -0.284075, -0.542779, -0.048438, 0.071906, -0.108732, 0.967821, 1.791633, 1.704818, 1.364777, 0.217876, -0.445118, -0.200242, -0.035981, -0.043764, -0.144667, -0.372499, -0.104196, 0.003848, 0.031949;
			4.065731, 0.075490, 0.120058, -0.045122, -0.130834, -0.062670, 0.103235, 0.038432, -0.258627, -0.348504, -0.621170, 3.011009, -0.575469, -0.399361, -0.260057, 0.022722, 0.345572, -0.264977, -0.112689, -0.183666, 0.238776, 0.027629, -0.019793, -0.369518, 0.041368, 0.003890, 0.160892, -0.437490, 0.053446, -0.035376, -0.007380, 0.024269, -0.168533, 0.045582, -0.043070, -0.061759, -0.025546, -0.027117, -0.089355, 0.013496, -0.040520, -0.039848, -0.055336;
			-0.015259, -0.351447, 0.182231, 0.053669, 0.338603, 0.252000, 0.108951, 0.210215, -1.013038, 0.341824, 0.379904, 0.075562, 0.179048, 0.132788, 0.345742, -2.396368, 0.298065, 0.482594, 0.327759, 0.205984, 0.429555, 0.316685, -1.511707, -0.172312, 0.428444, 0.321806, 0.397990, 0.217496, 0.192082, -1.163520, 0.021630, -1.450410, 0.189626, 0.258942, 0.258225, 0.186655, -0.368890, 0.271453, 0.328289, 0.170639, 0.252242, 0.250006, 0.177526;
			-0.064106, -0.210798, -0.084072, -0.200990, -0.104645, -0.166660, -0.155408, 0.382991, -0.322539, -0.281765, -0.048804, -0.508721, 0.165407, -0.094674, 1.399353, -0.369993, -0.295817, -0.087898, -0.495344, -0.659025, -0.209601, 2.024141, -0.126220, -0.165069, -0.412997, -0.320655, -0.298533, 0.215647, 1.715040, -0.131214, -0.102241, -0.440099, 0.070170, 0.445998, 0.219242, 1.316574, -0.202889, -0.223214, -0.166964, -0.317805, -0.390979, -0.284670, 0.151832;
			-0.061982, 0.098207, 0.342384, -0.037186, 0.206311, -0.482018, 0.182171, 0.008240, -0.214342, -0.079608, 0.568268, 0.236127, -1.079568, -0.197464, -0.087851, -0.063096, -0.107484, 0.075315, 1.501043, -1.170751, -0.673336, 0.007714, -0.043805, 0.071421, -0.172236, 0.061861, 1.923851, -0.462843, -0.113094, 0.005276, 0.124701, 0.236039, -0.118625, -0.717267, 0.923654, -0.180887, -0.046647, 0.010962, 0.044130, 0.015344, -0.641703, -0.302991, 0.510798;
			-0.099995, 0.176456, 0.195913, 0.138276, 0.194501, 0.187452, -0.017928, -0.106507, -0.204958, -0.417406, 0.144779, 0.345234, 0.331214, -0.024598, -0.429834, -0.054988, -0.135777, -0.373500, -0.712896, 0.795726, 0.062735, -0.608898, -0.213634, -0.314295, -0.417458, 0.472395, -0.340413, -0.602708, -0.278509, -0.156127, -0.360080, 0.400720, -0.687653, -0.571148, 0.009917, -0.084908, 0.844163, 1.498020, 1.173048, 0.869983, 0.045304, -0.366605, -0.112545;
			0.061793, -0.150014, 0.071884, 0.049893, -0.092852, -0.310731, -0.003072, 0.571779, -0.003529, -0.179661, -0.119232, 0.358278, -0.610294, 0.011590, 1.124678, -0.100981, -0.356908, -0.210024, -0.017841, 0.701002, -0.105886, 1.920412, -0.142186, -0.307546, -0.216803, 0.367974, -0.466944, -0.129683, 1.301596, -0.211575, -0.308191, 0.300554, -0.456978, -0.824156, -0.493624, 0.855146, -0.143586, -0.002098, -0.137513, -0.454744, -0.399712, -0.312762, 0.211280;
			0.015525, 0.041833, -0.048179, 0.006421, 0.209868, 0.158226, 0.245452, -0.010806, 0.263629, 0.204007, 0.149278, 0.131844, -0.014983, 0.542837, 0.035671, 0.166013, 0.094360, 0.107124, -0.142437, 0.126279, 0.425044, -0.245782, 0.151204, 0.035081, 0.118212, 0.300911, 0.099635, -0.385161, 0.086238, 0.158794, 0.011128, 0.268770, 0.146644, -0.148656, 0.267971, 0.050675, -0.963650, -1.743953, -1.257630, -1.484814, 0.063479, 1.294429, 0.119485;
			0.046898, -0.059270, 0.095614, -0.092866, 0.148298, -0.176326, -0.214035, -0.070372, 0.213870, -0.083153, -0.233726, 0.194545, -0.334771, -0.088795, -0.107262, 0.211518, 0.172300, -0.169135, -0.051174, -0.612364, -1.038251, 0.351811, 0.302397, 0.014941, -0.322662, 0.799400, -0.115944, -0.886554, 0.171797, 0.336146, -0.016156, 0.217667, 0.160412, 0.121453, -0.490662, -0.085431, 0.118069, 0.119145, 0.335211, 0.821318, 0.459247, -0.497725, 0.465311;
			0.001741, 0.131216, -0.009385, -0.215734, 0.159383, 0.093967, 0.238388, 0.107866, -0.314433, 0.676775, -0.362213, -0.059874, 0.263510, 0.041090, -0.004080, 0.077029, 0.187703, 2.420190, 0.295499, -0.273058, -0.021526, -0.343242, -0.176759, -0.301195, -0.339301, 1.355027, -0.701312, -0.385030, -0.159271, -0.063955, -0.132023, -0.237194, -0.370802, 0.986533, -0.340492, -0.226023, -0.210293, 0.021845, -0.232625, -0.549570, -0.482689, 0.645563, -0.480996;
			-0.005786, -0.036535, 0.512150, -0.193853, 0.082511, 0.333704, 0.061240, 0.071974, 0.025648, 0.186073, 1.372085, 0.050321, 0.541827, 0.257140, -0.311863, -0.447798, -0.351171, -0.451520, 1.389693, 0.595596, -0.171495, -0.579856, 0.168379, -0.270840, -0.677454, -0.542967, 1.382653, -0.241774, -0.433561, -0.162716, -0.380103, -0.107231, -0.612309, 0.293388, 0.405383, -0.201465, -0.380492, -0.269995, -0.429667, -0.687846, -0.145359, -0.184560, -0.122785;
			3.732799, 0.393233, -0.294192, -0.352953, 0.439528, 0.220672, -0.325883, -0.192772, -0.314837, 0.590048, 0.923352, -0.424792, -1.149057, 0.589973, 0.535254, 0.177838, -0.337333, -0.385183, 0.378586, 0.394613, -0.245926, -0.231810, -0.211310, 0.309293, 0.201260, -0.239979, -0.218715, 0.034605, 0.258905, 0.079883, -0.041500, -0.172998, 0.167498, 0.177283, -0.056753, -0.078659, 0.003291, -0.000914, 0.001316, -0.064154, -0.017064, 0.086915, 0.003243;
			-0.021749, 0.041930, 0.111038, 0.129719, 0.125701, 0.246941, 0.121760, -0.139530, -0.282353, -0.088727, -0.018955, 0.252901, 0.058292, 0.126904, 0.527618, -0.231518, -0.219581, 0.156545, -0.544421, -0.400470, 1.958469, -0.121108, -0.070161, 0.066199, -0.102424, -0.183762, 1.695182, -0.323016, -0.255808, -0.190593, -0.217780, -0.147568, 1.056625, -0.574445, -0.701982, -0.117378, -0.143095, -0.144713, 0.602117, -0.161625, -0.491905, -0.389147, -0.235610;
			-0.002932, 0.116909, 0.183454, 0.276995, 0.213163, 0.056336, 0.187324, 0.061348, 0.157527, 0.222099, 0.071959, 0.105939, 0.042983, 0.187047, 0.181105, 0.180941, 0.303783, 0.072174, 0.328965, 0.120853, 0.243719, 0.175102, 0.116480, 0.096610, 0.226680, 0.334804, 0.238726, 0.188337, 0.201461, 0.171952, 0.205034, 0.055147, 0.443518, 0.220798, 0.236795, 0.147591, 0.404981, 0.111471, -0.893384, -1.692651, -1.964811, -1.287822, -0.505072;
			-0.048016, -0.144592, 0.069353, 0.272453, 0.068880, 0.206107, 0.640356, 0.205184, -0.281053, -0.416389, -0.132099, 0.884970, 0.239335, 1.469766, -0.100391, -0.367843, -0.305759, -0.324786, -0.746313, -0.296761, 2.318177, -0.611150, -0.205363, -0.439618, -0.571842, -0.275046, -0.755443, 1.503254, -0.344904, -0.193355, -0.193049, -0.492955, -0.736425, -0.513084, 0.788556, -0.172894, -0.150793, -0.309545, -0.170964, -0.222643, 0.025964, 0.548683, -0.027023;
			0.019049, -0.037047, 0.049706, 0.036872, 0.030575, -0.254102, 0.096051, -0.080681, 0.350615, -0.178040, -0.706472, 0.595228, 0.341903, -0.359884, -0.245081, -0.015523, 0.847883, -0.772975, 0.246475, 0.367448, -0.377116, -0.313018, -0.142383, -0.176032, 1.675360, -0.320551, -0.244057, 0.086731, 0.059959, -0.240338, 0.114818, -0.837160, 0.714374, 0.345517, 0.188010, 0.467096, 0.090378, -0.158143, -0.600270, -0.394765, 0.159037, -0.229099, -0.418926;
			0.061621, -0.550487, 0.127712, 0.194900, 0.211605, 0.022059, -0.015202, 0.026524, -1.069828, 0.163710, 0.107408, -0.113472, 0.056113, -0.025707, 0.173789, -2.061833, 0.261615, 0.195963, 0.223356, 0.033644, 0.310163, 0.243549, -1.559587, 0.076671, -0.005273, 0.048004, 0.366818, 0.108487, 0.074793, -1.033559, 0.148216, 1.679970, 0.421961, -0.007502, 0.228323, 0.188669, -0.380031, 0.177969, 0.203933, 0.407813, 0.232084, 0.157664, 0.086698;
			0.006057, 0.759536, -0.407601, -0.662539, -1.314740, -0.846970, -0.620240, -0.571669, -1.109374, 0.263560, -0.077184, -0.469147, -0.782141, -0.685096, -0.375779, 1.514776, 0.618331, -0.552674, -0.037059, 0.080660, -0.140255, 0.216688, 0.837941, -0.400072, 0.841948, 0.009171, 0.487933, -0.244757, 0.194664, 0.648846, 0.553569, -0.197265, 0.338618, 0.178520, 0.109973, 0.232975, -0.961369, 0.798628, 0.727214, 0.910460, -0.297576, 0.548870, 0.340556;
			0.086641, -0.239896, -0.029956, -0.431863, -0.069223, -0.283343, 0.236495, -0.072144, -0.329570, 0.000115, -0.472379, -0.204654, 0.150432, -0.142065, -0.032621, 0.148697, -1.336701, -0.001901, 1.009802, -0.000356, 0.321446, 0.066263, 0.342105, 0.545645, -1.628797, 0.534038, 0.377598, 0.071069, 0.079117, 0.152072, 0.920101, 0.320768, -0.744616, 0.297437, 0.320242, 0.230523, 0.325868, 0.246263, 0.264255, 0.027564, -0.619292, -0.151824, -0.159797;
			-0.043492, 0.007464, 0.655843, 0.538913, 0.126015, 0.143681, 0.106389, -0.036305, -0.190076, 1.419772, 0.107161, -0.316102, -0.086448, -0.024639, -0.134201, -0.775098, 1.940319, -0.263289, 0.197517, -0.310863, -0.489734, -0.494610, -0.064867, 1.810169, 0.277905, -0.333343, -0.412155, -0.092688, -0.229343, -0.152111, 0.983770, -0.683284, -0.380192, -0.189339, -0.310062, -0.300588, 0.009136, 0.234850, -0.358453, -0.764703, -0.183658, -0.216812, -0.111146;
			-0.106027, 0.182451, 0.011725, -0.019373, 0.245167, 0.210929, -0.064763, 0.223342, 0.022099, 0.125496, -0.161150, 0.372003, 0.363971, -0.124842, -0.054596, 0.013642, -0.086816, 0.606244, 0.514652, 0.279343, -0.154985, -0.064406, 0.008420, 0.407086, -0.223195, -0.362653, -0.292815, 0.538381, -0.216198, -0.023437, -0.121176, -0.096376, -0.048705, -0.215314, -0.400906, -0.019850, -0.259647, -0.035700, 0.041863, -0.499562, -0.286975, 0.020858, -0.084546;
			0.021410, 0.153929, 0.190780, 0.077675, -0.323524, 0.002773, -0.063201, 0.293743, 0.198147, -0.134551, 0.026131, 0.230790, 0.233797, -0.067528, 0.134235, 0.420967, 0.106171, 0.234944, 0.172402, 0.288447, 0.284683, 0.284431, 0.228532, 0.213407, 0.308205, 0.569928, 0.334514, 0.277966, 0.113576, 0.125417, 0.128824, 0.479081, 0.323626, 0.249400, 0.343987, 0.341236, -1.023660, -1.163465, -1.855945, -1.793143, -0.491045, -0.881333, 0.286967;
			-3.991729, 0.481216, 0.381086, -0.277942, -0.536445, 0.200073, 0.362882, -0.378802, -0.470597, -0.853463, 1.350777, 0.400519, -0.460738, -0.638621, 0.268069, 0.289111, 0.169591, -0.210093, -0.368298, 0.301406, 0.223489, -0.018417, -0.301057, -0.071349, 0.210741, 0.306517, -0.410586, -0.216182, 0.110669, 0.061366, 0.105619, -0.140751, -0.102895, 0.110553, 0.140251, -0.080157, 0.004561, -0.070559, 0.013146, -0.025090, -0.086055, 0.004166, 0.005391;
			0.013934, 0.000932, -0.030408, 0.025969, 0.064430, -0.016359, -0.051847, 0.157620, 0.041985, 0.091241, 0.209340, 0.109073, 0.101551, 0.089165, 0.261771, 0.188948, 0.223810, 0.322471, 0.405451, 0.338631, 0.439456, 0.349589, 0.161386, 0.076498, 0.241816, 0.482382, 0.313099, 0.444224, 0.131089, 0.004734, -0.307857, -0.865083, -1.542171, -1.524775, -1.229910, -0.481792, 0.001110, 0.014491, 0.071449, 0.246262, 0.087837, 0.032655, 0.012979;
			0.001265, 0.021349, 0.140043, 0.193249, 1.449480, 0.046417, 0.065068, -0.076846, -0.007434, -0.302888, -0.109165, 1.887911, -0.089842, -0.245342, 0.040872, 0.456212, 0.239484, -0.550354, 2.124528, -0.610548, 0.206594, 0.437159, -0.201648, -0.368192, -0.791509, -4.154102, -0.567098, -0.398651, -0.180778, -0.094225, -0.209454, -0.339569, 1.141303, -0.115201, -0.145693, -0.015608, -0.056438, -0.002774, 0.154104, 0.874279, 0.168747, -0.063918, -0.021233;
			-2.678566, -0.165637, -0.051224, -0.099401, 0.096418, 0.128203, 0.050971, -0.175587, -0.190650, 0.309347, -0.136188, 0.600152, -1.725160, 0.123211, 0.227137, 0.044531, 0.212204, -0.353429, 0.044765, 0.165177, 0.382840, -0.511920, 0.059401, -0.240267, 0.383761, -0.061753, 0.037782, -0.142265, 0.269592, 0.161568, -0.037265, -0.049595, -0.161178, 0.214034, 0.029902, -0.168938, 0.066239, -0.067596, 0.071761, 0.156781, -0.019074, 0.070371, 0.107257;
			-3.615986, 0.382891, -0.526071, -0.004943, 0.138017, 0.162822, -0.549685, 0.129742, -0.391558, 0.925543, -0.984532, 0.908307, -0.959732, 1.118645, -0.527772, 0.004305, -0.078571, -0.125139, 0.270150, -0.282246, -0.208758, 0.132746, 0.145229, -0.061429, 0.223606, -0.551408, 0.329925, -0.021292, 0.165922, -0.130170, -0.151890, 0.250953, -0.185459, 0.159038, -0.163916, 0.011419, -0.073302, 0.191152, 0.084100, -0.051297, -0.004051, 0.099151, -0.155422
				""")

		self.theta2 = numpy.matrix("""
			-2.029150, -2.371098, 0.369746, -2.071351, -3.051468, 2.562886, 3.788085, -3.019396, -2.732541, -2.500113, -3.145558, 2.526331, 1.591746, -2.610270, -2.561247, 2.496617, -2.688258, 4.356012, -2.682443, -2.332880, 3.574912, 1.582689, 2.265756, -3.005081, -1.186712, 2.897375, -2.323892, 3.883714, 3.406733, -0.569153, -1.216606;
			-2.350716, 2.314704, -1.718933, 1.653383, 2.881803, 2.401869, -3.820614, 2.905872, 2.579130, 2.133293, 2.754343, -2.760551, -2.302414, 2.381751, 2.073648, 2.055584, 2.263108, -4.396869, 2.439749, 1.446536, -3.843084, -1.578867, -2.628301, 2.913844, 0.522145, -3.047224, -2.597870, -4.229494, -3.662692, -1.124020, -1.459787;
			2.387548, 0.125309, 1.962135, 0.634798, 0.178711, -8.425992, 0.251669, 0.056240, 0.151072, 0.646980, 0.523578, 0.375884, 1.121194, 0.290824, 0.527152, -7.177277, 0.804411, 0.099910, 0.114707, 1.416668, 0.344576, -0.074550, 0.743605, 0.054162, 0.553050, 0.501211, 6.815675, 0.524725, 0.563155, 3.311076, 4.913019
				""")

	def SetPlayerNumber(self, player):
		self.player = player
		

	def FormatBoard(self, board):
		b = numpy.zeros((board.rows*board.cols + 1))

		b[0] = 1

		for r in range(board.rows):
			for c in range(board.cols):
				if (board.board[r][c] == 1):
					b[r*board.cols + c + 1] = 1
				elif (board.board[r][c] == 2):
					b[r*board.cols + c + 1] = -1
				else:
					b[r*board.cols + c + 1] = 0

		b = numpy.matrix(b)
		return b
		

	def Sigmoid(self, z):
		return 1.0 / (1.0 + numpy.e**(-z));


	def EstimateBoardState(self, board):

		x = self.FormatBoard(board)

		h1_temp = self.theta1 * x.T
		
		h1 = numpy.zeros(h1_temp.shape[0] + 1)
		h1[0] = 1
		for i in range(h1_temp.shape[0]):
			h1[i+1] = self.Sigmoid(h1_temp[i,0])
		h1 = numpy.matrix(h1) 

		h2_temp = self.theta2 * h1.T
		h2 = numpy.zeros(h2_temp.shape[0])
		for i in range(h2_temp.shape[0]):
			h2[i] = self.Sigmoid(h2_temp[i,0])
		h2 = numpy.matrix(h2) 

		if self.player == 1:
			return ((h2[0,0] - h2[0,1]))
		else:
			return ((h2[0,1] - h2[0,0]))



	def GetMove(self, board):

		alpha = -1
		beta  = 1

		available_moves = board.GetAvailableMoves()
		
		new_player = self.player + 1
		if new_player > 2:
			new_player = 1

		moves_and_values = []
		for i in range(len(available_moves)):
			moves_and_values.append([available_moves[i],alpha])

		random.shuffle(moves_and_values)

		for i in range(len(moves_and_values)):
			move = moves_and_values[i][0]
			board.Move(self.player, move)
			value =  (self.GetMoveMinimax(board, new_player, self.depth-1, alpha, beta))
			moves_and_values[i][1] = value
			board.Unmove(move)

			alpha = max(alpha, value)
			
			if value >= beta:
				break # we have a winning solution

		#print("result", moves_and_values)

		for (m,v) in moves_and_values:
			if v == alpha:
				#print(moves_and_values)
				#print("making move", m)
				#print("")
				return m 


		return -1

	def GetMoveMinimax(self, board, player, depth, alpha, beta):

		winner = board.GetWinner()

		if winner != 0:
			if winner == self.player:
				return 1
			else:
				return -1


		if depth <= 0:
			return self.EstimateBoardState(board)

		available_moves = board.GetAvailableMoves()
		
		if available_moves == []:
			return 0

		new_player = player + 1
		if new_player > 2:
			new_player = 1

		if player == self.player: #maximize

			for m in available_moves:
				board.Move(player, m)
				alpha = max(alpha, self.GetMoveMinimax(board, new_player, depth-1, alpha, beta))
				board.Unmove(m)
			
				if beta <= alpha:
					break;

			return alpha 

		else: #minimize

			for m in available_moves:
				board.Move(player, m)
				beta = min(beta, self.GetMoveMinimax(board, new_player, depth-1, alpha, beta))
				board.Unmove(m)
			
				if beta <= alpha:
					break;

			return beta


if __name__ == "__main__": # simple demo

	a1 = MinimaxNNAI(6)
	a1.SetPlayerNumber(1)


	b = Board()

	b.Move(1, 6)
	b.Move(2, 1)
	b.Move(1, 6)
	b.Move(2, 1)
	b.Move(1, 6)
	b.Move(2, 2)

	b.Display()

	print(a1.EstimateBoardState(b))
	

