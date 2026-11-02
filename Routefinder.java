import java.util.*;

public class RouteFinder {

    static Map<String, List<String>> graph = new HashMap<>();

    static void addPath(String a, String b) {

        graph.putIfAbsent(a, new ArrayList<>());
        graph.putIfAbsent(b, new ArrayList<>());

        graph.get(a).add(b);
        graph.get(b).add(a);
    }

    static void findRoute(String start, String end) {

        Queue<List<String>> queue = new LinkedList<>();

        Set<String> visited = new HashSet<>();

        queue.add(Arrays.asList(start));

        visited.add(start);

        while (!queue.isEmpty()) {

            List<String> path = queue.poll();

            String current =
                path.get(path.size() - 1);

            if (current.equals(end)) {

                System.out.println(
                    String.join(" -> ", path)
                );

                return;
            }

            for (String next : graph.getOrDefault(
                    current, new ArrayList<>())) {

                if (!visited.contains(next)) {

                    visited.add(next);

                    List<String> newPath =
                        new ArrayList<>(path);

                    newPath.add(next);

                    queue.add(newPath);
                }
            }
        }

        System.out.println("No route found!");
    }

    public static void main(String[] args) {

        addPath("Main Gate", "Main Building");

        addPath("Main Building", "Library");

        addPath("Main Building", "Canteen");

        addPath("Library", "Auditorium");

        addPath("Canteen", "Parking Area");

        addPath("Auditorium", "Parking Area");

        if (args.length < 2) {
            System.out.println("Please select two locations.");
            return;
        }

        findRoute(args[0], args[1]);
    }
}