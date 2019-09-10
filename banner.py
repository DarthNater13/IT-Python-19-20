
def banner(title, author):
    title_length = len(title)
    by_line = f"By {author}"
    by_line_length = len(by_line)
    banner_length = max(title_length, by_line_length) + 4
    print(f"{'=' * banner_length}")
    print(f"{title.upper():^{banner_length}}")
    print(f"{by_line:^{banner_length}}")
    print(f"{'=' * banner_length}")
    print("")

if __name__=="__main__":
    banner("BANNER", "Nate Sherman")
    author = input("What is your name?")
    title = input("What is your quest?")
    banner(title, author)