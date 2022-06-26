SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

SELECT SUM(score)
FROM hacker_news;

SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;

SELECT (517 + 309 + 304 + 282) / 6366.0;

SELECT user, url
  FROM hacker_news
  WHERE url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

SELECT user, url, COUNT(url)
  FROM hacker_news
  WHERE url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
  GROUP BY user

SELECT CASE
  WHEN url LIKE 'github.com' THEN 'GitHub'
  WHEN url LIKE 'medium.com' THEN 'Medium'
  WHEN url LIKE 'nytimes.com' THEN 'New York Times'
  ELSE 'Other'
 END AS 'Source',
 COUNT(*)
FROM hacker_news
GROUP BY 1;

SELECT timestamp
FROM hacker_news
LIMIT 10;

SELECT timestamp,
  strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;
