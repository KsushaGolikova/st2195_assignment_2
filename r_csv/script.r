library(rvest)

# 1. URL страницы
url <- "https://en.wikipedia.org/wiki/Comma-separated_values"

# 2. Считываем HTML
page <- read_html(url)

# 3. Находим таблицы на странице
tables <- html_table(page, fill = TRUE)

# 4. Обычно таблица cars — первая или вторая, проверим:
cars <- tables[[1]]

# 5. Сохраняем как CSV
write.csv(cars, file = "cars_from_wiki.csv", row.names = FALSE)

