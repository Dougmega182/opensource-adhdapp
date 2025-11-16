export const AI = {
  taskBreakdown: async (task) => {
    if (!task) return [];
    return [
      `Break task "${task}" into steps`,
      "Focus for 5 minutes",
      "Create sub-tasks",
      "Start smallest step first"
    ];
  },

  brainDump: async (text) => {
    if (!text) return "";
    return `Summary:\n${text.slice(0, 50)}... (AI summary stub)`;
  }
};
