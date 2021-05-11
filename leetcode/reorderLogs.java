class Solution {



	public String[] reorderLogFiles(String[] logs) {



		Arrays.sort(logs, new Comparator<String>() {

			@Override
			public int compare(String log1, String log2) {
				if (isLetterLog(log1) && isLetterLog(log2)) {
					String logContent1 = log1.substring(log1.indexOf(" "), log1.length());
					String logContent2 = log2.substring(log2.indexOf(" "), log2.length());
					int contentCompare = 
				}
			}
		}
	}
}