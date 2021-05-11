class Solution {

	public String[] reorderLogFiles(String[] logs) {

		private boolean isLetterLog(String log) {
			return !Character.isDigit(log.charAt(log.length() - 1));
		}

		Arrays.sort(logs, new Comparator<String>() {

			@Override
			public int compare(String log1, String log2) {
				if (isLetterLog(log1) && isLetterLog(log2)) {
					String logContent1 = log1.substring(log1.indexOf(" "), log1.length());
					String logContent2 = log2.substring(log2.indexOf(" "), log2.length());
					int contentCompare = logContent1.compareTo(logContent2);

					if (contentCompare == 0) {
						String logId1 = log1.substring(0, log1.indexOf(" "));
						String logId2 = log2.substring(0, log2.indexOf(" "));

						return logId1.compareTo(logId2);
					}

					return contentCompare;

				}
			}

			if (!isLetterLog(log1) && isLetterLog(log2)) {
				return 1;
			}


			if (isLetterLog(log1) && !isLetterLog(log2)) {
				return -1;
			}

			return 0;
		}
	});

		return logs;
	}
}