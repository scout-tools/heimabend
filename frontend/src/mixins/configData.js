export const configData = {  // eslint-disable-line

  data: () => ({
    scoreConfig: [
      {
        techname: 'difficulty',
        name: 'Schwierigkeit',
        icon: 'mdi-head-snowflake-outline',
        color: 'green',
        rankings: [
          {
            score: 0,
            name: 'Einfach',
            techname: 'difficulty',
          },
          {
            score: 1,
            name: 'Einfach',
            techname: 'difficulty',
          },
          {
            score: 2,
            name: 'Mittel',
            techname: 'difficulty',
          },
          {
            score: 3,
            name: 'Mittel',
            techname: 'difficulty',
          },
          {
            score: 4,
            name: 'Schwer',
            techname: 'difficulty',
          },
        ],
      },
      {
        techname: 'executionTime',
        name: 'min. Zeit',
        icon: 'mdi-timer',
        color: 'blue',
        rankings: [
          {
            score: 0,
            name: '< 30 min',
            techname: 'executionTime',
          },
          {
            score: 1,
            name: '30 min',
            techname: 'executionTime',
          },
          {
            score: 2,
            name: '60 min',
            techname: 'executionTime',
          },
          {
            score: 3,
            name: '90 min',
            techname: 'executionTime',
          },
          {
            score: 4,
            name: '> 90 min',
            techname: 'executionTime',
          },
        ],
      },
      {
        techname: 'costsRating',
        name: 'Kosten',
        icon: 'mdi-currency-usd',
        color: 'orange',
        rankings: [
          {
            score: 0,
            name: '0,00 €',
            techname: 'costsRating',
          },
          {
            score: 1,
            name: '0,50 €',
            techname: 'costsRating',
          },
          {
            score: 2,
            name: '1,00 €',
            techname: 'costsRating',
          },
          {
            score: 3,
            name: '2,00 €',
            techname: 'costsRating',
          },
          {
            score: 4,
            name: '> 2,00 €',
            techname: 'costsRating',
          },
        ],
      },
      {
        techname: 'prepairationTime',
        name: 'Vorbereitung',
        icon: 'mdi-clock',
        color: 'red ligthen-1',
        rankings: [
          {
            score: 0,
            name: '0 min',
            techname: 'prepairationTime',
          },
          {
            score: 1,
            name: '5 min',
            techname: 'prepairationTime',
          },
          {
            score: 2,
            name: '30 min',
            techname: 'prepairationTime',
          },
          {
            score: 3,
            name: '60 min',
            techname: 'prepairationTime',
          },
          {
            score: 4,
            name: '> 60 min',
            techname: 'prepairationTime',
          },
        ],
      },
    ],
  }),
};
