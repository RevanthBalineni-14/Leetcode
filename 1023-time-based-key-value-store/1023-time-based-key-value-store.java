class TimeMap {
    HashMap<String, TreeMap<Integer, String>> h;
    public TimeMap() {
        h = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        h.computeIfAbsent(key, x->new TreeMap<>()).put(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        Integer nearest= (h.containsKey(key))?h.get(key).floorKey(timestamp):null;
        if(nearest==null)
            return "";
        return h.get(key).get(nearest);
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */