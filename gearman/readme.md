# Gearman

This role is more or less deprecated in favor of RabbitMQ or AWS SQS, however it should still function by-and-large if you need it. It is much simpler than RabbitMQ. However if you are going to be using it with PHP, you should absolutely use a pure-php library, and not any PECL C extension, as they are quite buggy.