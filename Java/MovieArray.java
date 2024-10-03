/**
 * A program to manage the episode info for a TV series.
 * By Anon. 26 Oct 2022
 * Version 1.
 */


import java.util.Scanner; // Needed to make Scanner available
import java.util.Random; // Needed to make Random available
import java.io.*; // Needed to make input/output files available


class Episode {
    int seasonNum;
    String title;
}

class EpisodeList {
    int numEpisodes;
    Episode[] episodes;
}

public class Main {
    /* Episode ADT: newEpisode, getEpisodeSeasonNum, getEpisodeTitle */

    // Return a new Episode with the given season number and title
    public static Episode newEpisode(int seasonNum, String title) {
        Episode e = new Episode();
        e.seasonNum = seasonNum;
        e.title = title;
        return e;
    }

    public static int getEpisodeSeasonNum(Episode s) {
        return s.seasonNum;
    }

    public static String getEpisodeTitle(Episode e) {
        return e.title;
    }

    /* EpisodeList ADT: newEpisodeList, addEpisode, printSeasonOfTitle, printAndCountSeason */

    // Return a new empty EpisodeList -- assume maximum 1000
    public static EpisodeList newEpisodeList() {
        EpisodeList l = new EpisodeList();
        l.numEpisodes = 0;
        l.episodes = new Episode[1000];
        return l;
    }

    // Add an Episode with the given season number and title to the EpisodeList
    public static EpisodeList addEpisode(EpisodeList l, int seasonNum, String title) {
        if (l.numEpisodes >= l.episodes.length) {
            return l;
        }
        Episode e = newEpisode(seasonNum, title);
        l.episodes[l.numEpisodes++] = e;
        return l;
    }

    // Print the season number of the Episode with the given title (if it exists)
    public static void printSeasonOfTitle(EpisodeList l, String title) {
        for (int i = 0; i < l.numEpisodes; i++) {
            Episode e = l.episodes[i];
            if (getEpisodeTitle(e).equals(title)) {
                System.out.println("Episode \"" + title + "\" was in season " + getEpisodeSeasonNum(e));
                return;
            }
        }
        System.out.println("Episode " + title + " not found.");
    }

    // Print the titles of all the episodes in the given season number and
    // the total number of episodes in that season
    public static void printAndCountSeason(EpisodeList l, int seasonNum) {
        int count = 0;
        for (int i = 0; i < l.numEpisodes; i++) {
            Episode e = l.episodes[i];
            if (getEpisodeSeasonNum(e) == seasonNum) {
                System.out.println("\"" + getEpisodeTitle(e) + "\"");
                count++;
            }
        }
        if (count == 0) {
            System.out.println("Unknown season number.");
        } else {
            System.out.println("Total episodes in season " + seasonNum + " is " + count);
        }
    }

    /* Main */
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        EpisodeList eps = newEpisodeList();
        menu(kb, eps);
    }

    // Main menu loop -- print menu, and repeatedly process options until (e)xit
    public static void menu(Scanner kb, EpisodeList eps) {
        System.out.println("(1) Add episode (2) Search for title " +
                           "(3) List season (4) Exit");
        String opt = "";
        while (!opt.equals("4")) {
            opt = askString(kb, "Enter option [1-4]: ");
            if (opt.equals("1")) {
                int seasonNum = askInt(kb, "Season number? ");
                String title = askString(kb, "Title? ");
                addEpisode(eps, seasonNum, title);
            } else if (opt.equals("2")) {
                String title = askString(kb, "Title to search for? ");
                printSeasonOfTitle(eps, title);
            } else if (opt.equals("3")) {
                int seasonNum = askInt(kb, "Season number to list? ");
                printAndCountSeason(eps, seasonNum);
            } else if (!opt.equals("4")) {
                System.out.println("Unknown option.");
            }
        }
    }

    /* Input helper methods */
    public static int askInt(Scanner kb, String prompt) {
        String line = askString(kb, prompt);
        return Integer.parseInt(line);
    }

    public static String askString(Scanner kb, String prompt) {
        System.out.print(prompt);
        return kb.nextLine();
    }
}
