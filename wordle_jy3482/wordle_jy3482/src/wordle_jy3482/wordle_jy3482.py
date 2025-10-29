
def validate_guess(guess, word_length=5):
    """
    Validate whether a guess is a valid Wordle guess.

    Parameters
    ----------
    guess : str
        The word guess to validate.
    word_length : int, optional
        Expected length of the word (default 5).

    Returns
    -------
    bool
        True if guess is valid, False otherwise.

    Notes
    -----
    Must be a string of length `word_length`, alphabetic-only, all lowercase.

    Examples
    --------
    >>> validate_guess("apple")
    True
    >>> validate_guess("Apple")
    False
    >>> validate_guess("apps")
    False
    >>> validate_guess("app1e")
    False
    >>> validate_guess(12345)
    False
    """
    if not isinstance(guess, str):
        return False
    if len(guess) != word_length:
        return False
    if not guess.isalpha():
        return False
    return guess.islower()


def check_guess(secret_word, guess):
    """
    Checks a guess against the secret word and returns color hints.

    Parameters
    ----------
    secret_word : str
        The secret word to guess.
    guess : str
        The player's guess.

    Returns
    -------
    list
        List of tuples (letter, color) where color is 'green', 'yellow', or 'gray'.
    """
    if len(secret_word) != len(guess):
        return []

    result = []
    secret_list = list(secret_word)
    guess_list = list(guess)

    # First pass: exact matches (green)
    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            result.append((guess_list[i], 'green'))
            secret_list[i] = None
            guess_list[i] = None
        else:
            result.append((guess_list[i], None))

    # Second pass: partial matches (yellow) or gray
    for i in range(len(guess_list)):
        if guess_list[i] is not None:
            if guess_list[i] in secret_list:
                result[i] = (guess_list[i], 'yellow')
                secret_list[secret_list.index(guess_list[i])] = None
            else:
                result[i] = (guess_list[i], 'gray')
    return result


def is_valid_word(word, word_list):
    """
    Check if a word exists in the valid word list (case-insensitive).

    Parameters
    ----------
    word : str
        The word to check.
    word_list : list
        List of valid words.

    Returns
    -------
    bool
        True if `word` is in `word_list` (ignoring case), False otherwise.

    Examples
    --------
    >>> wl = ["crane", "apple", "hello"]
    >>> is_valid_word("apple", wl)
    True
    >>> is_valid_word("APPLE", wl)
    True
    >>> is_valid_word("there", wl)
    False
    """
    return word.lower() in [w.lower() for w in word_list]


def calculate_game_score(guesses_used, max_guesses=6):
    """
    Calculates the score for a completed Wordle game.

    Parameters
    ----------
    guesses_used : int
        Number of guesses used to solve the puzzle.
    max_guesses : int, optional
        Maximum allowed guesses (default 6).

    Returns
    -------
    int
        Score from 0 to max_guesses (higher is better).
    """
    if guesses_used <= 0 or guesses_used > max_guesses:
        return 0
    return max_guesses - guesses_used + 1
