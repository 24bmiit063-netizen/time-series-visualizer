import unittest
import matplotlib.pyplot as plt
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot


class LinePlotTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = draw_line_plot()
        ax = fig.axes[0]

        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel(), "Page Views")
        self.assertEqual(
            ax.get_title(),
            "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        )


class BarPlotTestCase(unittest.TestCase):
    def test_bar_plot(self):
        fig = draw_bar_plot()
        ax = fig.axes[0]

        self.assertEqual(ax.get_xlabel(), "Years")
        self.assertEqual(ax.get_ylabel(), "Average Page Views")

        legend = ax.get_legend()
        self.assertIsNotNone(legend)
        self.assertEqual(legend.get_title().get_text(), "Months")


class BoxPlotTestCase(unittest.TestCase):
    def test_box_plot(self):
        fig = draw_box_plot()
        axes = fig.axes

        # Year-wise box plot
        self.assertEqual(
            axes[0].get_title(),
            "Year-wise Box Plot (Trend)"
        )
        self.assertEqual(axes[0].get_xlabel(), "Year")
        self.assertEqual(axes[0].get_ylabel(), "Page Views")

        # Month-wise box plot
        self.assertEqual(
            axes[1].get_title(),
            "Month-wise Box Plot (Seasonality)"
        )
        self.assertEqual(axes[1].get_xlabel(), "Month")
        self.assertEqual(axes[1].get_ylabel(), "Page Views")


if __name__ == "__main__":
    unittest.main()