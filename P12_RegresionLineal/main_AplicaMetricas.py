from P12_RegresionLineal import main_MetricasError as m

if __name__ == "__main__":
    X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Yprevista = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77]

    Yobservada = [2, 7, 12, 17, 23, 27, 32, 38, 44, 48, 54, 58, 64, 67, 73, 79]

    Yajustada = [2.8125, 7.8125, 12.8125, 17.8125, 22.8125, 27.8125, 32.8125, 37.8125,
                 42.8125, 47.8125, 52.8125, 57.8125, 62.8125, 67.8125, 72.8125, 77.8125]

    mse_prevista = m.mse(Yobservada, Yprevista)
    rmse_prevista = m.rmse(Yobservada, Yprevista)
    mae_prevista = m.mae(Yobservada, Yprevista)
    mape_prevista = m.mape(Yobservada, Yprevista)

    mse_ajustada = m.mse(Yobservada, Yajustada)
    rmse_ajustada = m.rmse(Yobservada, Yajustada)
    mae_ajustada = m.mae(Yobservada, Yajustada)
    mape_ajustada = m.mape(Yobservada, Yajustada)

    print("MSE: " + str(mse_prevista) + "\t" + str(mse_ajustada))
    print("RMSE: " + str(rmse_prevista) + "\t" + str(rmse_ajustada))
    print("MAE: " + str(mae_prevista) + "\t" + str(mae_ajustada))
    print("MAPE: " + str(mape_prevista) + "\t" + str(mape_ajustada))
