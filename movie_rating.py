UsersFavoriteMovie = input("What is your favorite movie?");
UsersRating = input(f"How would you rate {UsersFavoriteMovie}?");
errorMessage = "So I'll just give you a movie name of \"The Sound of Music\" and your arbitrary rating for this movie is 1."

def ratingDifference(UsersFavoriteMovie, UsersRating):
      from random import randint;
      MyRating = randint(1, 5);
      if (UsersRating < 1) or (UsersRating > 5.1):
         raise ValueError(dict(ValueError = ValueError, message = f"Your value of {UsersRating} MUST fall BETWEEN the range of 1 and 5!!!"));
      else:
         DifferenceBetweenUsersRatingAndMine = UsersRating - MyRating;
         return { 
            UsersFavoriteMovie
            : 
            dict(UsersRating = UsersRating, MyRating = MyRating, DifferenceBetweenUsersRatingAndMine = DifferenceBetweenUsersRatingAndMine, AbsoluteValueDifference = abs(DifferenceBetweenUsersRatingAndMine)) 
      }

# I will turn the bottom code into a function if I have time and rename ratingDifference to difference (serves one function: calculate difference).

try:
   UsersRating = int(UsersRating);
   if (UsersRating < 1) or (UsersRating > 5): raise ValueError();
except ValueError:
   print(f"VALUE ERROR: {ValueError} - Please enter a VALID WHOLE NUMBER between 1 and 5. Your number entered ({UsersRating}) is INVALID...\n", errorMessage, sep="");
except NameError:
   print(f"NAME ERROR: {NameError}. Please enter whole integers for your rating.\n", errorMessage, sep="");
except:
   print("You messed up somewhere...\n errorMessage", sep="");
finally:   
   print(ratingDifference(UsersFavoriteMovie = "The Sound of Music", UsersRating = 1));

