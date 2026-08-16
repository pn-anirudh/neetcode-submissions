class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String,List<String>> map = new HashMap<>();

        for(String i:strs){

            char[]t = i.toCharArray();
            Arrays.sort(t);
            String temp = new String(t);

            if(!map.containsKey(temp)){
                List<String> l = new ArrayList<String>();
                l.add(i);
                map.put(temp, l);
            }
            else{
                map.get(temp).add(i);
            }
        }

        return new ArrayList<>(map.values());


    }
}
